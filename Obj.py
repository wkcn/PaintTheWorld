import mygame
import pygame
import copy
from Defines import *

class Obj:
    def __init__(self, kwargs):
        self.name = kwargs["name"]
        self.realPos = copy.copy(kwargs["pos"]) 
        self.tarPos = copy.copy(kwargs["pos"]) 
        self.v = 1
        im = mygame.image.load("res/" + kwargs["tex"]) 
        if "scale" in kwargs:
            r = kwargs["scale"]
            w, h = im.get_size()
            tw = int(w * r)
            th = int(h * r)
            try:
                im = pygame.transform.smoothscale(im, (tw, th)).convert_alpha() 
            except:
                im = pygame.transform.scale(im, (tw, th)).convert_alpha() 
        self.tex = im
    def update(self, clock):
        for i in range(3):
            if (self.realPos[i] != self.tarPos[i]):
                if (self.realPos[i] < self.tarPos[i]):
                    self.realPos[i] += self.v * Normalize(clock)
                    if self.realPos[i] > self.tarPos[i]:
                        self.realPos[i] = self.tarPos[i]
                else:
                    self.realPos[i] -= self.v * Normalize(clock)
                    if self.realPos[i] < self.tarPos[i]:
                        self.realPos[i] = self.tarPos[i]
    def draw(self, screen):
        screen.blit(self.tex, (self.realx, self.realy))
    def moveto(self, target):
        for i in range(len(target)):
            self.tarPos[i] = target[i]
    @property
    def realx(self):
        return self.realPos[0]
    @property
    def realy(self):
        return self.realPos[1]
    @property
    def realz(self):
        return self.realPos[2]
    @realx.setter
    def realx(self, value):
        self.realPos[0] = value
    @realy.setter
    def realy(self, value):
        self.realPos[1] = value
    @realz.setter
    def realz(self, value):
        self.realPos[2] = value

