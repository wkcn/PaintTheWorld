#coding=utf-8
import time
import mygame
from pygame.locals import *
from sys import exit
from Mapper import *
from Action import *

mygame.init()
screen = mygame.screen

default_font = "arial"
font = mygame.font.SysFont(default_font, 20)

mp = Mapper()
Action.mp = mp
Action.screen = screen
mp.load("stage1.json")

cntClock = 0
cntFrame = 0
cntNetwork = 0
lastClock = time.time() * 1000
NowFPS = 0

while 1:
    for event in mygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit(0)
          

    nowClock = time.time() * 1000
    intervalClock = nowClock - lastClock
    lastClock = nowClock

    mp.update(intervalClock)
    screen.fill((0, 0, 0))
    mp.draw(screen)

    text_surface = font.render(u"FPS: %3.f" % NowFPS, True, (255, 0, 0))
    screen.blit_fix(text_surface, (0, 0))
    mygame.display.update()

    cntClock += intervalClock
    cntFrame += 1
    if cntClock >= 1000:
        fps = cntFrame * 1000.0 / cntClock
        NowFPS = fps
        cntClock = 0
        cntFrame = 0
    lastClock = nowClock
    
