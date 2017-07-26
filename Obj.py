import mygame
import pygame
import copy
from Defines import *

class Obj:
    FACE = None
    def __init__(self, args):
        self.name = args["name"]
        self.people = (self.name[:5] == "human")
        self.angle = 0
        self.scale = args.get("scale", 1.0)
        self.load_tex(args["tex"])
        self.realPos = copy.copy(args["pos"]) 
        self.tarPos = copy.copy(args["pos"]) 
        self.v = 1
        self.hide = args.get("hide", False) 
    def load_tex(self, filename):
        im = mygame.image.load("res/" + filename) 
        '''
        w, h = im.get_size()
        tw = int(w * self.scale)
        th = int(h * self.scale)
        try:
            im = pygame.transform.smoothscale(im, (tw, th)).convert_alpha() 
        except:
            im = pygame.transform.scale(im, (tw, th)).convert_alpha() 
        '''
        self.tex = im
        self.ow, self.oh = self.tex.get_size()
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
        if self.hide:
            return
        tex = pygame.transform.rotozoom(self.tex, self.angle, self.scale) 
        siz = tex.get_size()
        cx = self.realx - siz[0] / 2 + self.ow * self.scale / 2
        cy = self.realy - siz[1] / 2 + self.oh * self.scale / 2 
        screen.blit(tex, (cx, cy))
        if self.people and Obj.FACE is not None:
            screen.blit(Obj.FACE, (cx, cy)) 
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
    def rotate(self, v):
        self.angle += v
    def toscale(self, v):
        self.scale += v
