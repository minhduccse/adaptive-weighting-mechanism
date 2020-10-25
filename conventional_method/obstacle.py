import pygame as pg
from random import uniform
from random import randint


class Obstacle(pg.sprite.Sprite):
    image = pg.Surface((5, 5), pg.SRCALPHA)
    pg.draw.polygon(image, pg.Color('yellow'),
                    [(0, 0), (5, 0), (5,5), (0, 5)])

    max_x = 0
    max_y = 0


    def __init__(self,pos):
        super(Obstacle, self).__init__()

        if Obstacle.max_x == 0:
            info = pg.display.Info()
            Obstacle.max_x = info.current_w
            Obstacle.max_y= info.current_h

        self.image = Obstacle.image.copy()
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(
            pos[0],
            pos[1])
        self.rect = self.image.get_rect(center=self.pos)
