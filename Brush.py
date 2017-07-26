#coding=utf-8
import pygame
import mygame
import math
import numpy as np
from PIL import Image
import io
import model_api
import json

class Brush():
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size  = 1
        self.drawing = False
        self.last_pos = None
        self.space = 1
        self.npoints = []
        self.face = False

        self.x = 0
        self.y = 0
        self.w = 10000
        self.h = 10000
        self.t = 0
        self.label = ""

        self.bx = self.by = self.bw = self.bh = 0
        self.bim = None

        self.opened = False
        self.board_pic = None
        self.box_pic = None
        self.right = False
        self.predicted = True 
        self.xiaoming = pygame.image.load("./res/paint/face.png")
        self.ready = False 

        self.stop_clock = 0
        self.objkind = ""
        self.ys = []

    def open(self):
        self.opened = True
        self.ys = []
        self.t = 0.0
        self.stop_clock = 0
        self.npoints = []
    def close(self):
        self.opened = False

    def set_window(self, window):
        self.window = window
        full_window = [250,150,300,300]
        self.x, self.y, self.w, self.h = full_window
        self.bx, self.by, self.bw, self.bh = window
        #self.bim = self.screen.subsurface((self.bx, self.by), (self.bw, self.bh)) 
        if self.face:
            self.bim = pygame.transform.scale(pygame.image.load("res/board.png"), (800, 600))

        im = mygame.image.load("res/box.png") 
        self.box_pic = pygame.transform.scale(im, (300,300))
        self.xbox = pygame.transform.scale(pygame.image.load("./res/paint/xbox.png"), (self.window[2], self.window[3]))
        self.ready = True

    def start_draw(self, pos):
        self.drawing = True
        self.last_pos = pos
    def end_draw(self):
        self.drawing = False
        self.predicted = False

    def draw(self, pos):
        WIDTH = 0
        #if self.face:
        #    WIDTH = 3
        if not self.opened:
            return
        if self.ready:
            return
        if self.drawing:
            for p in self._get_points(pos):
                for ax in range(-WIDTH, WIDTH + 1):
                    for ay in range(-WIDTH, WIDTH + 1):
                        if abs(ax) + abs(ay) <= WIDTH:
                            q = (p[0] + ax, p[1] + ay)
                            if self.is_in_box(q):
                                self.npoints.append(q)
                pygame.draw.circle(self.screen,self.color, p, self.size)

            self.last_pos = pos

    def draw_bim(self):
        if self.face:
            self.t = 1.0
        x,y,w,h = self.get_cpos(self.t, (self.bx, self.by, self.bw, self.bh), (0, 0, 800, 600)) 
        #print (x,y,w,h)
        x = max(0, x)
        y = max(0, y)
        w = min(800 - x, w)
        h = min(600 - y, h)


        if self.bim is not None:
            #self.board_pic = pygame.transform.scale(self.bim, (w, h)).convert()
            self.board_pic = pygame.transform.scale(self.bim.subsurface((x,y),(w,h)), (800, 600))
        if not self.face:
            self.screen.blit(self.board_pic, (0, 0))

    def update(self, clock):
        if not self.opened:
            if self.t > 0:
                self.t = min(1.0, self.t - clock / 1000 * 2.5)
                self.draw_bim()
            return
        if self.ready:
            self.screen.blit(self.xbox, (self.window[0], self.window[1]))
            return


        # Open
        if self.t < 1:
            self.t = min(1.0, self.t + clock / 1000 * 1.5)
            self.draw_bim()
            return
        if not self.face:
            self.screen.blit(self.board_pic, (0, 0))

        if self.face:
            self.screen.blit(self.xiaoming, (165, 0))
        if self.box_pic is not None:
            self.screen.blit(self.box_pic, (250, 150))

        if self.drawing:
            self.stop_clock = 0
        else:
            if not self.predicted:
                self.stop_clock += clock
                if self.stop_clock > 3000:
                    ys = self.predict()
                    print (self.objkind, ys)
                    if type(self.objkind) == list:
                        for o in self.objkind:
                            if o in ys:
                                self.right = True
                                self.label = o
                                break
                    else:
                        if self.objkind in ys:
                            self.right = True
                            self.label = self.objkind
                    self.stop_clock = 0
                    self.predicted = True
                    self.ys = ys

        for p in self.npoints:
            pygame.draw.circle(self.screen,self.color, p, self.size)
    def set_objkind(self, objkind):
        self.objkind = objkind
        self.right = False
    def get_bpos(self, t, s, b):
        sx,sy,sw,sh = s
        bx,by,bw,bh = b
        sw = max(1, sw)
        sh = max(1, sh)
        w = int(sw * (1.0 - t) + bw * t)
        h = int(sh * (1.0 - t) + bh * t)
        zh = int(w / sw * sh)
        zw = int(h / sh * sw)

        if w > zw:
            h = zh
        if h > zh:
            w = zw

        w = max(1, w)
        h = max(1, h)
        x = max(int((1.0 - t) * sx + t * bx), 0)
        y = max(int((1.0 - t) * sy + t * by), 0)
        return (x,y,w,h)


    def get_cpos(self, t, s, b):
        sx,sy,sw,sh = s
        bx,by,bw,bh = b
        x = int(sx * t + bx * (1.0 - t))
        y = int(sy * t + by * (1.0 - t))
        w = int(sw * t + bw * (1.0 - t))
        h = int(sh * t + bh * (1.0 - t))
        #h = w * 600 / 800
        #w = h * 800 / 600
        return (x,y,w,h)
    def predict(self):
        # Check The Kind
        print ("Predict...")
        im = self.get_pic()
        pim = Image.fromarray(np.uint8(im))
        output = io.BytesIO()
        pim.save(output, format = "JPEG")
        hex_data = output.getvalue()
        text = model_api.predict(hex_data)
        js = json.loads(text)
        return js["class_name"]

    def is_in_box(self, p):
        return (self.x <= p[0] < self.x + self.w and self.y <= p[1] < self.y + self.h)

    def _get_points(self, pos):
        """ Get all points between last_point ~ now_point. """
        points = [ (self.last_pos[0], self.last_pos[1]) ]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for i in range(int(length)):
            points.append((points[-1][0] + step_x, points[-1][1] + step_y))
        points = map(lambda x:(int(0.5+x[0]), int(0.5+x[1])), points)
        # return light-weight, uniq list
        return list(set(points))

    def clear(self):
        self.npoints = []
    def thick(self, WIDTH):
        tmp = []
        for p in self.npoints:
            for ax in range(-WIDTH, WIDTH + 1):
                for ay in range(-WIDTH, WIDTH + 1):
                    if abs(ax) + abs(ay) <= WIDTH:
                        q = (p[0] + ax, p[1] + ay)
                        if self.is_in_box(q):
                            tmp.append(q)
        self.npoints.extend(tmp)
    def get_pic(self):
        im = np.ones((self.h, self.w)).astype(np.uint8) * 255
        ah = aw = 0
        for p in self.npoints:
            im[int(p[1] - self.y + ah), int(p[0] - self.x + aw)] = 0
        return im
