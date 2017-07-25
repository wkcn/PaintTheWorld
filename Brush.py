#coding=utf-8
import pygame
import math
import numpy as np

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

        self.opened = False

    def open(self):
        self.opened = True
    def close(self):
        self.opened = False

    def set_window(self, window):
        self.x, self.y, self.w, self.h = window

    def start_draw(self, pos):
        self.drawing = True
        self.last_pos = pos
    def end_draw(self):
        self.drawing = False

    def draw(self, pos):
        if not self.opened:
            return
        if self.drawing:
            for p in self._get_points(pos):
                self.npoints.append(p)
                pygame.draw.circle(self.screen,self.color, p, self.size)

            self.last_pos = pos
    def update(self):
        if not self.opened:
            return
        for p in self.npoints:
            pygame.draw.circle(self.screen,self.color, p, self.size)

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
        for i in xrange(int(length)):
            points.append((points[-1][0] + step_x, points[-1][1] + step_y))
        points = filter(self.is_in_box, map(lambda x:(int(0.5+x[0]), int(0.5+x[1])), points))
        # return light-weight, uniq list
        return list(set(points))

    def clear(self):
        self.npoints = []
    def get_pic(self):
        im = np.zeros((self.h, self.w)).astype(np.uint8)
        for p in self.npoints:
            im[int(p[1] - self.y), int(p[0] - self.x)] = 255
        return im
