import json
from Obj import *
from Action import *

class Mapper:
    def __init__(self):
        self.clear()
    def clear(self):
        self.data = None
        self.clock = 0
        self.objs = []
        self.objs_map = dict()
        self.actions = []
        self.paused = False
        self.brush = None
        self.caption = ""
        self.black = False
        self.pause_time = 0
    def load(self, filename):
        self.clear()
        fin = open(filename, "r")
        s = fin.read()
        fin.close()
        self.data = json.loads(s)
        # Load Objects
        for so in self.data["obj"]:
            o = Obj(so)
            self.objs.append(o)
            self.objs_map[o.name] = o
        # Load Actions
        for ac in self.data["actions"]:
            a = Action(ac)
            self.actions.append(a)
        self.actions.sort(key = lambda x:x.start)
    def update(self, clock):
        if self.paused:
            for a in self.actions:
                if a.hold:
                    a.update(self.clock)
            return

        for o in self.objs:
            o.update(clock)

        self.clock += clock

        for a in self.actions:
            a.update(self.clock)
            if self.paused:
                break
        self.actions = [a for a in self.actions if not a.dead]
    def draw(self, screen):
        # layer
        self.objs.sort(key = lambda o: o.realz)
        for o in self.objs:
            o.draw(screen)
    def get_obj(self, name):
        return self.objs_map[name]
    def goon(self):
        self.paused = False
    def pause(self):
        self.paused = True
