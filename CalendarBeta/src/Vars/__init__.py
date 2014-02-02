import pygame, copy
pygame.init()
'''
Created on Aug 18, 2013

by blacKnight
'''

WINWIDTH = 1000
WINHEIGHT = 1000
FPS = 60 # frames per second to update the screen

BLACK   =     (0,0,0)
WHITE   =     (255,255,255)
DARKRED =     (175,0,0)
GREEN   =     (0,255,0)
TOOLBARGREY = (50,50,50)
DARKGREY = (100,100,100)
MEDGREY = (150,150,150)
LIGHTGREY = (200,200,200)

GREEKALPH = 'alpha bravo charlie delta echo foxtrot golf hotel india juliett kilo lima mike november oscar papa quebec romeo sierra tango uniform victor whiskey x-ray yankee zulu'.split()
OLDGREEKALPH = 'able boy cast dog easy fox george have item jig king love mikey nan oboe pup quack rush sail tare unit vice watch xeno yoke zed'.split()
NEWLOGINIT = ['Exercise','Eat','Games']

AFONTSIZE = 20
AFONT = pygame.font.Font('courier.ttf',AFONTSIZE)
BGTIMEFONTSIZE = 12
TIMEFONT = pygame.font.Font('courier.ttf',BGTIMEFONTSIZE)
CLOCKSIZE = 30
CLOCKFONT = pygame.font.Font('courier.ttf',CLOCKSIZE)

DISPLAYSURF = pygame.display.set_mode((WINWIDTH,WINHEIGHT))

HALFX = WINWIDTH/2
TITLEBARHEIGHT = WINHEIGHT/20
TOOLBARHEIGHT = WINHEIGHT/15
BGMIDLINEOFFSET = 20
BGMIDLINETHICK = 4
BGSLOTHEIGHT = ((WINHEIGHT-TOOLBARHEIGHT-TITLEBARHEIGHT)/24)
BGSLOTSTARTY = TITLEBARHEIGHT+((BGSLOTHEIGHT-BGTIMEFONTSIZE)/2)
BGSLOTSTARTX = 10

CLOCKPOS = [10,10]
DATEPOS = [0,0]
VIEWMONTHPOS = [100,0]
