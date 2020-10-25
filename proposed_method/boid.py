import pygame as pg
from random import uniform
from random import randint
import globalvariables



class Boid(pg.sprite.Sprite):

    perception = 50
    crowding = 40
    avoiding = 40

    crowding_weight = 28
    avoiding_weight = 28

    crowding_transform = crowding_weight/crowding
    avoiding_transform = avoiding_weight/avoiding

    max_x = 0
    max_y = 0
    # CONFIG
    speed = 1.2
    min_speed = 1
    max_speed = 1.2
    max_ideal_neighb = 6
    ############################################################
    ###   best forces values for dynamic weighting factors ##### 
    max_force = .03 #.03
    separation_max_force = .03   #.03

    ############################################################

    def __init__(self, id):
        super(Boid,self).__init__()
        if Boid.max_x == 0:
            info = pg.display.Info()
            Boid.max_x = info.current_w
            Boid.max_y= info.current_h

        self.leader = 0
        self.id = id
        if self.leader ==1:
            self.connected = 1
        else: 
            self.connected = 0
        self.image = pg.Surface((11, 11), pg.SRCALPHA)
        pg.draw.circle(self.image, pg.Color('orange'), (6, 6), 4)
        self.rect = self.image.get_rect()
        self.pos = pg.math.Vector2(
            uniform(30, Boid.max_x/6),
            uniform(30, Boid.max_y/6))

        self.rect = self.image.get_rect(center=self.pos)

        self.vel = pg.math.Vector2()

        self.accel = pg.math.Vector2()
#################################################################################
###   Reynolds rules + custom rule (avoid) with dynamic weighting factors   #####
    def separation(self, boids):
        v = pg.Vector2()
        weight = 0
        if boids:
            for boid in boids:
                dist = self.pos.distance_to(boid.pos)
                if dist < self.crowding:
                    vn = pg.Vector2(boid.pos - self.pos)
                    vn = (self.crowding-dist*(dist/self.crowding))*vn.normalize()
                    v -= vn
                    weight = max(weight,self.crowding-dist*(dist/self.crowding))
            v = self.separation_force(v)
        return v*weight


    def alignment(self, boids):
        v = pg.Vector2()
        if boids:
            for boid in boids:
                v += boid.vel
            v /= len(boids)
            v = self.clamp_force(v)
            return v*self.max_ideal_neighb/len(boids)
        return v


    def avoid(self, obs):
        v = pg.Vector2()
        weight = 0
        if obs:
            for ob in obs:
                dist = self.pos.distance_to(ob.pos)
                if dist < self.avoiding:
                    vn = pg.Vector2(ob.pos - self.pos)
                    vn = (self.avoiding-dist*(dist/self.avoiding))*vn.normalize()
                    v -= vn
                    weight = max(weight,self.avoiding-dist*(dist/self.avoiding))
            v = self.separation_force(v)
            weight=weight*self.avoiding_transform
        return v*weight

    def cohesion(self, boids):
        v = pg.Vector2()
        if boids:
            for boid in boids:
                v += boid.pos
            v /= len(boids)
            v -= self.pos
            v = self.clamp_force(v)
            return v*self.max_ideal_neighb/len(boids)
        return v

    def checktarget(self):
        if self.pos.distance_to(globalvariables.target[0].pos)< self.perception:
            return True
        else:
            return False

    def checkcolision_neigh(self,boids):
        if boids:
            for boid in boids:
                if self.pos.distance_to(boid.pos)< 9 and boid != self:
                    return True
        else:
            return False

    def checkcolision_ob(self,obs):
        if obs:
            for ob in obs:
                if self.pos.distance_to(ob.pos)< 9:
                    return True
        else:
            return False

##################################################################################
    def migration(self,boids):
        steering = pg.Vector2()
        
        if globalvariables.click == 1:
            if globalvariables.target:
                steering = pg.Vector2(globalvariables.target[0].pos - self.pos)
                steering = self.clamp_force(steering)
                if boids:
                    return steering*(self.max_ideal_neighb + self.max_ideal_neighb/len(boids))
                else: 
                    return steering*(self.max_ideal_neighb)
            else:
                return steering
        else:
            return steering

    def update(self, boids, obs):
        # update velocity
        neighbors = self.get_neighbors(boids)
        obs_neighbors = self.get_obs_neighbors(obs)

        separation = pg.Vector2()
        alignment = pg.Vector2()
        cohesion = pg.Vector2()
        avoid = pg.Vector2()
        migration = pg.Vector2()

        avoid = self.avoid(obs_neighbors)
        separation = self.separation(neighbors)
        alignment = self.alignment(neighbors)
        cohesion = self.cohesion(neighbors)
        migration = self.migration(neighbors)
        self.accel = separation +  avoid + alignment + cohesion + migration

        # move and turn
        self.pos += self.vel

        self.wrap()
        _, angle = self.vel.as_polar()
        self.vel += self.accel
        
        # enforce speed limit
        while self.vel.magnitude() < self.min_speed:
            _, angle = self.vel.as_polar()
            self.vel.from_polar((self.min_speed * 1.1, angle))
        if self.vel.magnitude() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)
        
        # make boid
        if self.leader ==0:
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.rect = self.image.get_rect(center=self.pos)

        return avoid.magnitude(), separation.magnitude(), alignment.magnitude(), cohesion.magnitude(), migration.magnitude()
        
    def wrap(self):
        if self.pos.x < 0:
            self.pos.x += Boid.max_x

        elif self.pos.x > Boid.max_x:
            self.pos.x -= Boid.max_x

        if self.pos.y < 0:
            self.pos.y += Boid.max_y

        elif self.pos.y > Boid.max_y:
            self.pos.y -= Boid.max_y

    def get_neighbors(self, boids):
        neighbors = []
        for boid in boids:
            if boid != self:
                dist = self.pos - boid.pos
                if dist.magnitude() < self.perception:
                    neighbors.append(boid)
        return neighbors

    def get_obs_neighbors(self, obs):
        obs_neighbors = []
        for ob in obs:
            if ob != self:
                dist = self.pos - ob.pos
                if dist.magnitude() < self.perception:
                    obs_neighbors.append(ob)
        return obs_neighbors

    def clamp_force(self, force):
        if force.magnitude() > 0:
            force = force.normalize()
        return force

    def separation_force(self, force):
        if force.magnitude() > 0:
            force = force.normalize()
        return force
