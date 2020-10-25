import pygame as pg
from random import uniform
from random import randint

class Targetpoint(pg.sprite.Sprite):
    perception =  50
    image = pg.Surface((perception*2, perception*2), pg.SRCALPHA)
    pg.draw.circle(image, pg.Color('green'), (perception, perception), 5 ,1)
    pg.draw.circle(image, pg.Color('white'), (perception, perception), perception, 1)

    max_x = 0
    max_y = 0


    def __init__(self,pos):
        super(Targetpoint, self).__init__()

        if Targetpoint.max_x == 0:
            info = pg.display.Info()
            Targetpoint.max_x = info.current_w
            Targetpoint.max_y= info.current_h

        self.image = Targetpoint.image.copy()
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(
            pos[0],
            pos[1])
        self.rect = self.image.get_rect(center=self.pos)
