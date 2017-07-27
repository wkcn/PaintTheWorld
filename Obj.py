import mygame
import pygame
import copy
from Defines import *

class Obj:
    def __init__(self, args):
        self.name = args["name"]
        self.people = (self.name[:5] == "human")
        self.angle = 0
        self.face = None
        self.scale = args.get("scale", 1.0)
        self.tex = None
        self.load_tex(args.get("tex", None))
        self.realPos = copy.copy(args["pos"]) 
        self.tarPos = copy.copy(args["pos"]) 
        self.v = 1
        self.hide = args.get("hide", False) 
    def load_tex(self, filename):
        if filename is None:
            return
        im = mygame.image.load("res/" + filename) 
        self.filename = filename
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
        if self.face is not None:
            self.tex.blit(self.face, (85, 150))
        self.ow, self.oh = self.tex.get_size()
    def set_face(self, face):
        self.face = face
        self.load_tex(self.filename)
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
        if self.tex is None:
            return
        tex = pygame.transform.rotozoom(self.tex, self.angle, self.scale) 
        siz = tex.get_size()
        cx = self.realx - siz[0] / 2 + self.ow * self.scale / 2
        cy = self.realy - siz[1] / 2 + self.oh * self.scale / 2 
        screen.blit(tex, (cx, cy))
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
