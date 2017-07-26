#coding=utf-8
import time
import mygame
from pygame.locals import *
from sys import exit
from Mapper import *
from Action import *
from Obj import *
import Brush
from PIL import Image
import io
import numpy as np

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

brush = Brush.Brush(screen.surface)
mp.brush = brush

default_font = "arial"
font = mygame.font.SysFont(default_font, 20)
#default_font2 = "sourcehansanscn"
#font2 = mygame.font.SysFont(default_font2, 40)

font2 = mygame.font.Font("./res/fzht.ttf", 50)

last_mouse_pos = (0,0)

def print_pos(p):
    global last_mouse_pos
    lp = last_mouse_pos
    offset = (p[0] - lp[0], p[1] - lp[1])
    g = (int(p[0] + screen.display_x), int(p[1] + screen.display_y))
    print ("global_pos: %s, mouse_pos: %s, offset: %s" % (str(g), str(p), str(offset)))
    last_mouse_pos = p

while 1:
    for event in mygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit(0)
            elif event.key == K_SPACE:
                brush.right = True
        elif brush.opened:
            if event.type == MOUSEBUTTONDOWN:
                # Left Button
                if event.button == 1:
                    brush.start_draw(event.pos)
                    print_pos(event.pos)
                else:
                    brush.clear()
                    mp.caption = ""
            elif event.type == MOUSEMOTION:
                brush.draw(event.pos)
            elif event.type == MOUSEBUTTONUP:
                brush.end_draw()
        else:
            if event.type == MOUSEBUTTONDOWN:
                print_pos(event.pos)

    if brush.opened:
        if brush.right:
            if brush.face:
                # draw face!
                bim = brush.get_pic().astype(np.uint8)
                r,c = bim.shape
                im = np.zeros((r,c,4)).astype(np.uint8)
                im[bim == 0,3] = 255
                pim = Image.fromarray(im)
                pim.save("./res/face.png")
                Obj.FACE = pygame.image.load("./res/face.png")
                pass
            brush.close()
            mp.goon()
            mp.caption = "这是%s :-)" % brush.label
        if brush.predicted:
            if len(brush.ys) > 0:
                if not brush.right:
                    mp.caption = "这是%s吗" % brush.ys[0]
              

    nowClock = time.time() * 1000
    intervalClock = nowClock - lastClock
    lastClock = nowClock

    mp.update(intervalClock)
    screen.fill((255, 255, 255))
    mp.draw(screen)

    brush.update(intervalClock)

    '''
    text_surface = font.render(u"FPS: %3.f" % NowFPS, True, (255, 0, 0))
    screen.blit_fix(text_surface, (0, 0))
    '''

    caption_surface = font2.render(mp.caption, True, (255, 255, 255))
    _len = len(mp.caption)
    x = (800 - _len * 50) / 2
    screen.blit_fix(caption_surface, (x, 520))

    mygame.display.update()

    cntClock += intervalClock
    cntFrame += 1
    if cntClock >= 1000:
        fps = cntFrame * 1000.0 / cntClock
        NowFPS = fps
        cntClock = 0
        cntFrame = 0
    lastClock = nowClock
    
