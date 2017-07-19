import mygame
import pygame
import copy
from Defines import *

class Obj:
    def __init__(self, args):
        self.name = args["name"]
        self.realPos = copy.copy(args["pos"]) 
        self.tarPos = copy.copy(args["pos"]) 
        self.v = 1
        self.scale = args.get("scale", 1.0)
        self.load_tex(args["tex"])
    def load_tex(self, filename):
        im = mygame.image.load("res/" + filename) 
        w, h = im.get_size()
        tw = int(w * self.scale)
        th = int(h * self.scale)
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

