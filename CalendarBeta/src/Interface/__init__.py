import random, sys, copy, os, pygame, math, Main, Vars
from pygame.locals import *

    
def GetInterfaceActions(mousePastLoc):
    a = []
    for event in pygame.event.get():
        if event.type == QUIT:
            Main.terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                a.append(('a',chr(27)))
            elif event.key == K_0:
                a.append(('k','0'))
            elif event.key == K_1:
                a.append(('k','1'))
            elif event.key == K_2:
                a.append(('k','2'))
            elif event.key == K_3:
                a.append(('k','3'))
            elif event.key == K_4:
                a.append(('k','4'))
            elif event.key == K_5:
                a.append(('k','5'))
            elif event.key == K_6:
                a.append(('k','6'))
            elif event.key == K_7:
                a.append(('k','7'))
            elif event.key == K_8:
                a.append(('k','8'))
            elif event.key == K_9:
                a.append(('k','9'))
            elif event.key == K_a:
                a.append(('k','a'))
            elif event.key == K_b:
                a.append(('k','b'))
            elif event.key == K_c:
                a.append(('k','c'))
            elif event.key == K_d:
                a.append(('k','d'))
            elif event.key == K_e:
                a.append(('k','e'))
            elif event.key == K_f:
                a.append(('k','f'))
            elif event.key == K_g:
                a.append(('k','g'))
            elif event.key == K_h:
                a.append(('k','h'))
            elif event.key == K_i:
                a.append(('k','i'))
            elif event.key == K_j:
                a.append(('k','j'))
            elif event.key == K_k:
                a.append(('k','k'))
            elif event.key == K_l:
                a.append(('k','l'))
            elif event.key == K_m:
                a.append(('k','m'))
            elif event.key == K_n:
                a.append(('k','n'))
            elif event.key == K_o:
                a.append(('k','o'))
            elif event.key == K_p:
                a.append(('k','p'))
            elif event.key == K_q:
                a.append(('k','q'))
            elif event.key == K_r:
                a.append(('k','r'))
            elif event.key == K_s:
                a.append(('k','s'))
            elif event.key == K_t:
                a.append(('k','t'))
            elif event.key == K_u:
                a.append(('k','u'))
            elif event.key == K_v:
                a.append(('k','v'))
            elif event.key == K_w:
                a.append(('k','w'))
            elif event.key == K_x:
                a.append(('k','x'))
            elif event.key == K_y:
                a.append(('k','y'))
            elif event.key == K_z:
                a.append(('k','z'))
            elif event.key == K_KP0:
                a.append(('k','0'))
            elif event.key == K_KP1:
                a.append(('k','1'))
            elif event.key == K_KP2:
                a.append(('k','2'))
            elif event.key == K_KP3:
                a.append(('k','3'))
            elif event.key == K_KP4:
                a.append(('k','4'))
            elif event.key == K_KP5:
                a.append(('k','5'))
            elif event.key == K_KP6:
                a.append(('k','6'))
            elif event.key == K_KP7:
                a.append(('k','7'))
            elif event.key == K_KP8:
                a.append(('k','8'))
            elif event.key == K_KP9:
                a.append(('k','9'))
            elif event.key == K_RSHIFT or event.key == K_LSHIFT:
                a.append(('s',chr(15)))
            elif event.key == K_BACKSPACE:
                a.append(('a',chr(8)))
            elif event.key == K_TAB:
                a.append(('a',chr(9)))
            elif event.key == K_RETURN:
                a.append(('a',chr(13)))
            elif event.key == K_SPACE:
                a.append(('k',chr(32)))
            elif event.key == K_SLASH:
                a.append(('k',chr(47)))
            elif event.key == K_PERIOD:
                a.append(('k',chr(46)))
            elif event.key == K_LEFTBRACKET:
                a.append(('k',chr(91)))
            elif event.key == K_RIGHTBRACKET:
                a.append(('k',chr(93)))
            elif event.key == K_DELETE:
                a.append(('a',chr(127)))
            elif event.key == K_UP:
                a.append(('a','W'))
            elif event.key == K_DOWN:
                a.append(('a','S'))
            elif event.key == K_RIGHT:
                a.append(('a','D'))
            elif event.key == K_LEFT:
                a.append(('a','A'))
            elif event.key == K_RCTRL or event.key == K_LCTRL:
                a.append(('s','Z'))
            elif event.key == K_COMMA:
                a.append(('k',','))
            elif event.key == K_MINUS:
                a.append(('k','-'))
            elif event.key == K_EQUALS:
                a.append(('k','='))
            elif event.key == K_RALT or event.key == K_LALT:
                a.append(('s','C'))
        elif event.type == KEYUP:
            if event.key == K_RSHIFT or event.key == K_LSHIFT:
                a.append(('h',chr(14)))
            elif event.key == K_RCTRL or event.key == K_LCTRL:
                a.append(('h','X'))
            elif event.key == K_RALT or event.key == K_LALT:
                a.append(('h','V'))
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            a.append(('m','M',mousex,mousey,mousePastLoc))
            mousePastLoc = [mousex,mousey]
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            a.append(('m','U',mousex,mousey,mousePastLoc))
            mousePastLoc = [mousex,mousey]
        elif event.type == MOUSEBUTTONDOWN:
            mousex,mousey = event.pos
            a.append(('m','J',mousex,mousey,mousePastLoc))
            mousePastLoc = [mousex,mousey]
    return [a,mousePastLoc]

def IsTransDn(item): #ctrl, shift, alt
    if len(item)>2:
        return False
    else:
        if item == 'Z':
            return True
        elif item == 'C':
            return True
        elif item == chr(15):
            return True
    return False
    
def IsTransUp(item):
    if len(item)>2:
        return False
    else:
        if item == chr(14):
            return True
        elif item == 'X':
            return True
        elif item == 'V':
            return True
    return False

def IsActionDn(item): #del, backspace, tab, return, esc, up, down, left, right
    if len(item)>2:
        return False
    else:
        if item == chr(8):
            return True
        elif item == chr(9):
            return True
        elif item == chr(127):
            return True
        elif item == chr(13):
            return True
        elif item == chr(27):
            return True
        elif item == 'W':
            return True
        elif item == 'S':
            return True
        elif item == 'D':
            return True
        elif item == 'A':
            return True
    return False

def IsLetterDn(item): # everything else
    if len(item)>2:
        return False
    else:
        if IsTransUp(item) == True:
            return False 
        if IsTransDn(item) == True:
            return False
        if IsActionDn(item) == True:
            return False
    return True

def MouseAction(item):
    if len(item)>2:
        return True
    else:
        return False
    
def DetermineType(item):
    if len(item)>2:
        return 0
    elif IsTransUp(item) == True:
        return 1
    elif IsTransDn(item) == True:
        return 2
    elif IsActionDn(item) == True:
        return 3
    else:
        return 4
        