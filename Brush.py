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

        self.x = 0
        self.y = 0
        self.w = 10000
        self.h = 10000

        self.bx = self.by = self.bw = self.bh = 0

        self.opened = False
        self.board_pic = None
        self.box_pic = None
        self.right = False
        self.predicted = True 

        self.stop_clock = 0
        self.objkind = ""

    def open(self):
        self.opened = True
    def close(self):
        self.opened = False

    def set_window(self, window):
        full_window = [250,150,300,300]
        self.x, self.y, self.w, self.h = full_window
        self.bx, self.by, self.bw, self.bh = window
        im = mygame.image.load("res/" + "board.png") 
        self.board_pic = pygame.transform.scale(im, (800, 600)).convert()
        self.board_pic.set_alpha(100)

        im = mygame.image.load("res/" + "board.png") 
        self.box_pic = pygame.transform.scale(im, (self.bw, self.bh)).convert()

    def start_draw(self, pos):
        self.drawing = True
        self.last_pos = pos
    def end_draw(self):
        self.drawing = False
        self.predicted = False

    def draw(self, pos):
        WIDTH = 0
        if not self.opened:
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
    def update(self, clock):
        if not self.opened:
            return
        if self.drawing:
            self.stop_clock = 0
        else:
            if not self.predicted:
                self.stop_clock += clock
                if self.stop_clock > 3000:
                    ys = self.predict()
                    print (self.objkind, ys)
                    if self.objkind in ys:
                        self.right = True
                    self.stop_clock = 0
                    self.predicted = True

        if self.board_pic is not None:
            self.screen.blit(self.board_pic, (0, 0))
        if self.box_pic is not None:
            self.screen.blit(self.box_pic, (self.bx, self.by))
        for p in self.npoints:
            pygame.draw.circle(self.screen,self.color, p, self.size)
    def set_objkind(self, objkind):
        self.objkind = objkind
        self.right = False
    def predict(self):
        # Check The Kind
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
    def get_pic(self):
        im = np.ones((self.h, self.w)).astype(np.uint8) * 255
        ah = aw = 0
        for p in self.npoints:
            im[int(p[1] - self.y + ah), int(p[0] - self.x + aw)] = 0
        return im
