#coding=utf-8
import time
import mygame
from pygame.locals import *
from sys import exit
from Mapper import *
from Action import *
from Obj import *
import Brush
from PIL import Image, ImageFilter
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

# DEBUG
# PLAY SPEED
ratio = 1

while 1:
    for event in mygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit(0)
            elif event.key == K_SPACE:
                if not brush.ready:
                    brush.right = True
                else:
                    brush.ready = False
            elif event.key == K_p:
                if mp.paused:
                    mp.goon()
                    lastClock = None
                else:
                    mp.pause()
        elif brush.opened:
            if not brush.ready:
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
                    brush.ready = False 
        else:
            if event.type == MOUSEBUTTONDOWN:
                print_pos(event.pos)

    if brush.opened:
        if brush.right:
            if brush.face:
                # draw face!
                print ("draw face")
                brush.thick(2)
                bim = brush.get_pic().astype(np.uint8)
                r,c = bim.shape

                '''
                b = (bim == 0)
                for i in range(1, 2):
                    b[:-i,:] |= b[i:,:] 
                    b[i:,:] |= b[:-i,:] 
                    b[:, :-i] |= b[:, i:] 
                    b[:, i:] |= b[:, :-i] 
                bim = ((~b) * 255).astype(np.uint8)
                '''


                im = np.zeros((r,c,4)).astype(np.uint8)
                im[bim == 0,3] = 255
                pim = Image.fromarray(im).filter(ImageFilter.EDGE_ENHANCE)
                pim.save("./res/face.png")
                for o in mp.objs:
                    if o.people:
                        o.set_face(pygame.image.load("./res/face.png"))
                print ("face ok")
            brush.close()
            mp.goon()
            lastClock = None
            mp.caption = "这是%s :-)" % brush.label
            mp.black = False
        if brush.predicted:
            if len(brush.ys) > 0:
                if not brush.right:
                    mp.caption = "这是%s吗" % brush.ys[0]
                    mp.black = False
              

    nowClock = time.time() * 1000
    if lastClock is None:
        lastClock = nowClock
    intervalClock = max(0, nowClock - lastClock)
    lastClock = nowClock

    mp.update(intervalClock * ratio)
    screen.fill((255, 255, 255))
    mp.draw(screen)

    brush.update(intervalClock)

    '''
    text_surface = font.render(u"FPS: %3.f" % NowFPS, True, (255, 0, 0))
    screen.blit_fix(text_surface, (0, 0))
    '''

    if mp.black:
        caption_surface = font2.render(mp.caption, True, (0,0,0))
    else:
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
    
