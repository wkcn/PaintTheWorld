class Action:
    mp = None
    def __init__(self, arg):
        self.kind = arg["type"]
        self.obj = Action.mp.get_obj(arg["obj"])
        self.start = arg["start"] * 1000
        self.end = arg.get("end", 10240) * 1000
        self.dead = False
        self.running = False
        if self.kind == "move":
            self.offset = arg["offset"]
        elif self.kind == "change_tex":
            self.tex = arg["tex"]
        elif self.kind == "rotate":
            self.v = arg.get("v", 1)
    def update(self, clock):
        if clock > self.end:
            self.dead = True
            return
        if clock < self.start:
            return
        if not self.running:
            # First
            if self.kind == "move":
                tar = (self.obj.realx + self.offset[0], self.obj.realy + self.offset[1])
                self.obj.moveto(tar)
            elif self.kind == "change_tex":
                self.obj.load_tex(self.tex)
        # trigger
        if self.kind == "rotate":
            self.obj.rotate(self.v * clock / 180.0 * 3.1415)
        self.running = True
