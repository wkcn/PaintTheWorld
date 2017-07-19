class Action:
    mp = None
    def __init__(self, arg):
        self.kind = arg["type"]
        self.obj = Action.mp.get_obj(arg["obj"])
        self.start = arg["start"] * 1000
        self.end = arg["end"] * 1000
        self.dead = False
        self.running = False
        if self.kind == "move":
            self.offset = arg["offset"]
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
        self.running = True