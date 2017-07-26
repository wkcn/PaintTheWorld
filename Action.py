from Defines import *

class Action:
    mp = None
    screen = None
    def __init__(self, arg):
        self.kind = arg["type"]
        if "obj" in arg:
            self.obj = Action.mp.get_obj(arg["obj"])
        self.start = arg["start"] * 1000
        self.end = arg.get("end", 10240) * 1000
        self.hold = arg.get("hold", False)
        self.dead = False
        self.running = False
        if self.kind == "move":
            self.offset = arg["offset"]
            self.v = arg.get("v", 1) 
        elif self.kind == "change_tex":
            self.tex = arg["tex"]
        elif self.kind in ["rotate", "scale"]:
            self.v = arg.get("v", 1)
            self.tovalue = arg.get("tovalue", None)
        elif self.kind == "move_screen":
            self.offset = arg["offset"]
            self.v = arg["v"]
        elif self.kind == "bezier":
            self.seq = arg["seq"]
            self.v = arg["v"]
            self.t = 0.0
        elif self.kind == "draw":
            self.window = arg["window"]
            self.objkind = arg["kind"]
            self.face = arg.get("face", False)
            self.rep = arg.get("rep", None)
        elif self.kind == "caption":
            self.caption = arg["caption"]
            self.black = arg.get("black", False)
        elif self.kind in ["hide", "show"]:
            pass
        else:
            raise TypeError("Unknown Type %s" % self.kind)
    def update(self, clock):
        # ms
        if clock > self.end:
            if self.kind == "caption":
                if Action.mp.caption == self.caption:
                    Action.mp.caption = ""
            self.dead = True
            return
        if clock < self.start:
            return
        if not self.running:
            # First
            if self.kind == "move":
                tar = (self.obj.realx + self.offset[0], self.obj.realy + self.offset[1])
                self.obj.v = self.v
                self.obj.moveto(tar)
            elif self.kind == "change_tex":
                self.obj.load_tex(self.tex)
            elif self.kind == "hide":
                self.obj.hide = True
            elif self.kind == "show":
                self.obj.hide = False 
            elif self.kind == "pause":
                Action.mp.pause()
            elif self.kind == "draw":
                Action.mp.brush.face = self.face
                Action.mp.brush.bim = Action.screen.surface
                Action.mp.brush.set_window(self.window)
                bx, by, bw, bh = self.window
                #Action.mp.brush.bim = Action.screen.surface.subsurface((bx, by), (bw, bh)) 

                Action.mp.brush.open()
                Action.mp.brush.set_objkind(self.objkind)
                Action.mp.pause() 
                Action.mp.brush.obj = self.rep
            elif self.kind == "caption":
                Action.mp.caption = self.caption
                Action.mp.black = self.black
                if self.end == -1:
                    Action.mp.pause()

        # trigger
        if self.kind == "rotate":
            self.obj.rotate(self.v * clock / 180.0 * 3.1415 / 1000)
            if self.tovalue is not None:
                d = abs(self.tovalue - self.obj.angle)
                if d <= 1:
                    self.obj.angle = self.tovalue
                    self.dead = True
        elif self.kind == "scale":
            self.obj.toscale(self.v * clock / 1000)
            if self.tovalue is not None:
                d = self.tovalue - self.obj.scale
                if d * self.v < 0:
                    self.obj.scale = self.tovalue
                    self.dead = True
        elif self.kind == "move_screen":
            screen = Action.screen
            dx = self.offset[0] - screen.display_x
            dy = self.offset[1] - screen.display_y
            ok = False
            if dx * self.v > 0:
                screen.display_x += self.v * clock / 1000.0
                ok = True
            if dy * self.v > 0:
                screen.display_y += self.v * clock / 1000.0
                ok = True
            self.dead = not ok
        elif self.kind == "bezier":
            self.t = min(self.t + self.v * clock / 1000.0, 1.0)
            if self.t >= 1:
                self.dead = True
            else:
                bx, by = (bezier(self.seq, self.t))
                self.obj.realPos[0] = self.obj.tarPos[0] = bx
                self.obj.realPos[1] = self.obj.tarPos[1] = by


        self.running = True
