import json
from Obj import *

class Mapper:
    def __init__(self):
        self.clear()
    def clear(self):
        self.data = None
        self.clock = 0
        self.objs = []
        self.objs_map = dict()
    def load(self, filename):
        self.clear()
        fin = open(filename, "r")
        s = fin.read()
        fin.close()
        self.data = json.loads(s)
        for so in self.data["obj"]:
            o = Obj(so)
            self.objs.append(o)
            self.objs_map[o.name] = o
    def update(self, clock):
        self.clock += clock
        for o in self.objs:
            o.update(clock)
    def draw(self, screen):
        # layer
        self.objs.sort(key = lambda o: o.realz)
        for o in self.objs:
            o.draw(screen)
