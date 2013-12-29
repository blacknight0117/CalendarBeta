import random, sys, copy, os, pygame, math, time, Vars, calendar, Interface
from pygame.locals import *

class InputBox():
    def __init__(self,loc,sizex=10,sizey=1,offset = [0,0],BGcolor = Vars.WHITE,TextColor = Vars.BLACK,OutlineColor = Vars.MEDGREY,numberBool=False):
        self.heightLetter = sizey
        self.widthLetter = sizex
        self.height = Vars.AFONTSIZE*sizey+2
        self.width = 0 
        self.location = loc
        self.BGcolor = BGcolor
        self.TextColor = TextColor
        self.OutlineColor = OutlineColor
        self.font = Vars.AFONT
        self.data = ''
        self.dataSplit = []
        self.number = 0
        self.numberBool = numberBool
        self.BGrect = 0
        self.textSurf = []
        self.textRect = []
        self.offset = offset
        self.LoadData()
        self.cursor = -1
        self.selected = False
        self.ctrlDown = False
        self.shftDown = False
        
    def LoadData(self):
        temp = ''
        for i in range(self.widthLetter):
            temp = temp+'X'
        self.textSurf = self.font.render(temp,True,Vars.WHITE,Vars.WHITE)
        self.textRect = self.textSurf.get_rect()
        self.width = self.textRect.width+2
        self.BGrect = pygame.Rect(self.offset[0]+self.location[0]+1,self.offset[1]+self.location[1]+1, self.width-2,self.height-2)
        self.data = ''
        self.dataSplit = []
        self.number = 0
        if self.numberBool == True:
            self.heightLetter = 1
        
    def Move(self,newOffset):
        change = self.offset-newOffset
        self.BGrect.topleft = self.BGrect.topleft+change
        self.textrect.topleft = self.textrect.topleft+change
    
    def Select(self):
        self.selected = True
        self.cursor = 0
    
    def Deselect(self):
        self.selected = False
        self.cursor = -1
    
    def Display(self):
        OutlineRect = pygame.Rect(self.BGrect.left-1,self.BGrect.top-1,self.width,self.height)
        pygame.draw.rect(Vars.DISPLAYSURF,self.OutlineColor,OutlineRect)
        pygame.draw.rect(Vars.DISPLAYSURF,self.BGcolor,self.BGrect)
        Vars.DISPLAYSURF.blit(self.textSurf,self.textRect)
        #draw highlight if on selected
        #draw a cursor
    def MouseBtnDown(self,loc):
        #if BGrect.collide == true
            #select
        #else
            #deselect
        pass
            
    def Input(self,inputActions):
        for i in range(len(inputActions)):
            type = Interface.DetermineType(inputActions[i])
            if type == 0:
                pass
            elif type == 1:
                if self.selected == True:
                    #go through transup
                    pass
            elif type == 2:
                if self.selected == True:
                    #go through transdn
                    pass
            elif type == 3:
                if self.selected == True:
                    #go through actiondn
                    pass
            elif type == 4:
                if self.selected == True:
                    self.data = self.data+inputActions[i]
                
    def Retrieve(self):
        if self.numberBool==False:
            return self.data
        else:
            return self.number

class DropBox():
    def __init__(self,loc,atype,size=0,offset,BGcolor=Vars.LIGHTGREY,TextColor=Vars.BLACK,HovColor = Vars.WHITE):
        self.loc = loc
        self.type = atype
        self.present = -1
        self.presRect
        self.presTextSurf
        self.presTextRect
        self.presTriangle
        self.presTriRect
        self.offset = offset
        self.shown = False
        self.BGcolor = BGcolor
        self.TextColor = TextColor
        self.HovColor = HovColor
        if size > 5:
            self.height = size
            self.font = pygame.font.Font('courier.ttf',self.height)
        else:
            self.size = Vars.AFONTSIZE
            self.font = Vars.AFONT
        self.data = []
        self.rects = []
        self.surfs = []
        self.allRect
        self.presentHover = -1
        
        self.loadDate()
        
    def LoadData(self):
        if self.type == 'newloginit':
            self.data = copy.deepcopy(Vars.NEWLOGINIT)
            tempSurf = self.font.render(self.data[0],True,Vars.WHITE,Vars.WHITE)
            tempRect = tempSurf.get_rect()
            newRect = pygame.Rect(self.offset[0]+self.loc[0],self.offset[1]+self.loc[1],(tempRect.width+self.size),(tempRect.height))
            self.presRect = copy.deepcopy(newRect)
            self.presTriRect = ((newRect.right-self.size),newRect.top,self.size,self.size)
            self.presTriangle = Triangle(tempRect,Vars.BLACK,0,'right',3)
            for i in range(len(self.data)):
                tempSurf = self.font.render(self.data[i],True,self.BGcolor,self.TextColor)
                tempRect = tempSurf.get_rect()
                if i == 0:
                    tempRect.topleft = self.presTriRect.bottomleft
                else:
                    tempRect.topleft = self.rects[i-1].bottomleft
                self.rects.append(tempRect)
                self.surfs.append(tempSurf)
            self.allRect = pygame.Rect(self.rects[0].left,self.rects[0].top,self.rects[0].width,(self.rects[len(self.rects)].bottom-self.rects[0].top))
        
    def Display(self):
        pygame.draw.rect(Vars.DISPLAYSURF,self.BGcolor,self.presRect)
        if self.shown == False:
            pygame.draw.rect(Vars.DISPLAYSURF,self.TextColor,self.presTriRect)
        else:
            pygame.draw.rect(Vars.DISPLAYSURF,self.BGColor,self.presTriRect)
        self.presTriangle.Display()
        if self.present > -1:
            Vars.DISPLAYSURF.blit(self.presTextSurf,self.presTextRect)
        if self.shown == True:
            pygame.draw.rect(Vars.DISPLAYSURF,self.BGcolor,self.allRect)
            for i in range(len(self.data)):
                Vars.DISPLAYSURF.blit(self.surfs[i],self.rects[i])

    def Move(self,newOffset):
        change = self.offset - newOffset
        self.presRect.topleft = self.presRect.topleft + change
        self.presTriRect = self.presTriRect + change
        self.presTriangle.Move(change)
        for i in range(len(self.rects)):
            self.rects[i].topleft = self.rects[i].topleft + change
        self.allRect = self.allRect + change
    
    def LocCollide(self,loc,clicked):
        if self.shown:
            if self.allRect.collidepoint(loc[0],loc[1]):
                if clicked == 1:
                    self.MouseClick(loc)
                elif clicked == 2:
                    self.MouseMotion(loc)
                return True
        if self.presRect.collidepoint(loc[0],loc[1]):
            if clicked == 1:
                self.MouseClick(loc)
            elif clicked == 2:
                self.MouseMotions(loc)
            return True
        if self.presentHover>-1:
            self.surfs[self.presentHover] = self.font.render(self.data[self.presentHover],True,self.BGcolor,self.TextColor)
            self.presentHover = -1
        return False
    
    def MouseMotion(self,mouseLoc):
        if self.shown == True:
            found = False
            for i in range(self.rects):
                if self.rects[i].collidepoint(mouseLoc[0],mouseLoc[1])==True:
                    self.surfs[i] = self.font.render(self.data[i],True,self.HovColor,self.TextColor)
                    self.presentHover = i
                    found = True
                    break
            if found == False:
                if self.presentHover>-1:
                    self.surfs[self.presentHover] = self.font.render(self.data[self.presentHover],True,self.BGcolor,self.TextColor)
                    self.presentHover = -1
                    
    def MouseClick(self,clickLoc):
        if self.shown == True:
            for i in range(len(self.rects)):
                if self.rects[i].collidepoint(clickLoc[0],clickLoc[1]):
                    self.present = i
                    self.presTextSurf = copy.deepcopy(self.surfs[i])
                    self.presTextRect = copy.deepcopy(self.rects[i])
                    self.presTextRect.topleft = self.presRect.topleft
                    return self.data[i]
        if self.presTriRect.collidepoint(clickLoc[0],clickLoc[1]):
            if self.shown == True:
                self.presTriangle.PointRight()
                self.presTriangle.color = self.BGcolor
            else:
                self.presTriangle.PointDown()
                self.presTriangle.color = self.Textcolor

class Triangle():
    def __init__(self,aRect,color,thickness,direction,inset):
        self.color = color
        self.thickness = thickness
        self.boundingBox = copy.deepcopy(aRect)
        self.direction = direction
        self.inset = inset
        self.points = []
        
        if direction == 'up':
            self.PointUp()
        elif direction == 'down':
            self.PointDown()
        elif direction == 'right':
            self.PointRight()
        elif direction == 'left':
            self.PointLeft()
        
    def Display(self):
        temp = copy.deepcopy(self.points)
        for i in range(len(temp)):
            temp[i] = temp[i]+self.offset
        pygame.draw.polygon(Vars.DISPLAYSURF,self.color,temp)
    
    def PointUp(self):
        self.direction = 'up'
        temp = []
        temp.append((self.boundingBox.bottomleft[0]+self.inset[0],self.boundingBox.bottomleft[1]-self.inset[1]))
        temp.append((self.boundingBox.bottomright[0]-self.inset[0],self.boundingBox.bottomright[1]-self.inset[1]))
        temp.append((self.boundingBox.centerx,self.boundingBox.top+self.inset[1]))
        self.points = copy.deepcopy(temp)
        
    def PointDown(self):
        self.direction = 'down'
        temp = []
        temp.append((self.boundingBox.topleft[0]+self.inset[0],self.boundingBox.topleft[1]+self.inset[1]))
        temp.append((self.boundingBox.topright[0]-self.inset[0],self.boundingBox.topright[1]+self.inset[1]))
        temp.append((self.boundingBox.centerx,self.boundingBox.bottom+self.inset[1]))
        self.points = copy.deepcopy(temp)
        
    def PointRight(self):
        self.direction = 'left'
        temp = []
        temp.append((self.boundingBox.topright[0]-self.inset[0],self.boundingBox.topright[1]+self.inset[1]))
        temp.append((self.boundingBox.bottomright[0]-self.inset[0],self.boundingBox.bottomright[1]-self.inset[1]))
        temp.append((self.boundingBox.left+self.inset[1],self.boundingBox.centery))
        self.points = copy.deepcopy(temp)
        
    def PointLeft(self):
        self.direction = 'right'
        temp = []
        temp.append((self.boundingBox.topleft[0]+self.inset[0],self.boundingBox.topleft[1]+self.inset[1]))
        temp.append((self.boundingBox.bottomleft[0]+self.inset[0],self.boundingBox.bottomleft[1]-self.inset[1]))
        temp.append((self.boundingBox.right+self.inset[1],self.boundingBox.centery))
        self.points = copy.deepcopy(temp)
    
    def Move(self,change):
        self.boundingBox.topleft = self.boundingBox.topleft + change
        if self.directions == 'up':
            self.PointUp()
        elif self.directions == 'down':
            self.PointDown()
        elif self.directions == 'right':
            self.PointRight()
        elif self.directions == 'left':
            self.PointLeft()
            
class Window():
    def __init__(self,loc,aType,BGcolor=Vars.WHITE,FrontColor=Vars.MEDGREY,TextColor=Vars.BLACK):
        self.type = aType
        self.data = []
        self.boxes = []
        self.drops = []
        self.offset = loc
        self.titleHeight = 25
        self.height
        self.width
        self.closeRect
        self.minimRect
        self.title = ''
        self.moving = False
        self.BGrect
        self.titleRect
        self.spacing = 5
        self.BGcolor = BGcolor
        self.FrontColor = FrontColor
        self.TextColor = TextColor
        
        self.LoadData()
        
        
    def LoadData(self):
        #also used to reload data if type changes
        if self.type == 'newlog':
            self.title = 'New Log'
            self.width = 200
            self.height = 100
            self.MakeRects()
            aLoc = (self.titleRect.left+self.spacing,self.titleRect.bottom+self.spacing)
            tempObj = DropBox(aLoc,'newloginit')
    
    def MakeRects(self):
        #need to create checking for outside of bounds
        self.BGrect = pygame.Rect(self.offset[0],self.offset[1],self.width,self.height)
        self.titleRect = pygame.Rect(self.BGrect.left,self.BGRect.top,self.BGrect.width,self.titleHeight)
        btnSize = self.titleHeight-6
        self.closeRect = pygame.Rect((self.BGrect.right-6-btnSize),(self.BGrect.top-3),btnSize,btnSize)
        self.minimRect = copy.deepcopy(self.closeRect)
        self.minimRect.left = self.minimRect.left-6-btnSize
        
    def DisplayTitleBar(self):
        pass
    
class Background():
    def __init__(self):
        self.windows = []
        self.toolButtons = []
        self.toolbarRect
        self.titlebarRect
        self.startTime = 4
        self.timeSurfs = []
        self.timeRects = []
        self.bgColorRects = []
        self.clockSurf
        self.clockRect
    
    def Init(self):
        self.SetTimeRects()
        self.SetBgRects()
        self.UpdateClock()
        self.clockRect = self.clockSurf.get_rect()
        self.clockRect.topleft = Vars.CLOCKPOS
    
    def Draw(self):
        Vars.DISPLAYSURF.fill(Vars.WHITE)
        pygame.draw.rect(Vars.DISPLAYSURF,Vars.TOOLBARGREY,self.toolbarRect)
        pygame.draw.rect(Vars.DISPLAYSURF,Vars.TOOLBARGREY,self.titlebarRect)
        for i in range(len(self.bgColorRects)):
            if i%2 == 0:
                pygame.draw.rect(Vars.DISPLAYSURF,Vars.WHITE,self.bgColorRects[i])
            else:
                pygame.draw.rect(Vars.DISPLAYSURF,Vars.LIGHTGREY,self.bgColorRects[i])
        pygame.draw.line(Vars.DISPLAYSURF,Vars.TOOLBARGREY,(Vars.HALFX,Vars.TITLEBARHEIGHT+Vars.BGMIDLINEOFFSET),(Vars.HALFX,Vars.WINHEIGHT-Vars.TOOLBARHEIGHT-Vars.BGMIDLINEOFFSET),Vars.BGMIDLINETHICK)
        for i in range(len(self.toolButtons)):
            self.toolButtons[i].Draw()
        for i in range(len(self.timeRects)):
            Vars.DISPLAYSURF.blit(self.timeSurfs[i],self.timeRects[i])
        Vars.DISPLAYSURF.blit(self.clockSurf,self.clockRect)
        #draw other titlebar elements
        #month, day, arrow buttons, current date
        
    def UpdateClock(self):
        localTime = time.localtime(time.time())
        timeList = list(localTime)
        
        if timeList[3]<10:
            stringClock = '0'+ str(timeList[3]) + ':'
        else:
            stringClock = str(timeList[3]) + ':'
        if timeList[4]<10:
            stringClock = stringClock + '0'+ str(timeList[4]) + ':'
        else:
            stringClock = stringClock + str(timeList[4]) + ':'
        if timeList[5]<10:
            stringClock = stringClock + '0' + str(timeList[5])
        else:
            stringClock = stringClock + str(timeList[5])
            
        self.clockSurf = Vars.CLOCKFONT.render(stringClock,True,Vars.BLACK,Vars.TOOLBARGREY)
        
    def SetBgRects(self):
        temp = pygame.Rect(0,0,Vars.WINWIDTH,Vars.BGSLOTHEIGHT)
        for i in range(24):
            self.bgColorRects[i] = copy.deepcopy(temp)
            if i == 0:
                self.bgColorRects[i].top = Vars.TITLEBARHEIGHT
            else:
                self.bgColorRects[i].top = self.bgColorRects[i-1].bottom
                
    def SetTimeRects(self):
        a = self.startTime
        for i in range(24):
            if a > 23:
                a = 0
            self.timeSurfs[i] = Vars.TIMEFONT.render(a+':00',True,Vars.TOOLBARGREY,Vars.WHITE)
            self.timeRects[i] =self.timeSurfs[i].get_rect()
            if i == 0 :
                self.timeRects[i].topleft = [Vars.BGSLOTSTARTX,Vars.BGSLOTSTARTY]
            else:
                self.timeRects[i].topleft = self.timeRects[i-1].topleft + [0,Vars.BGSLOTHEIGHT]
        
        
def InterfaceHandler():
    def __init__(self):
        self.ctrl = False
        self.shft = False
        self.alt = False
        self.theWindow
        self.theSelected
        self.theGUI
        self.interactions
        self.mousePastLoc
        
        self.Setup()
    
    def Setup(self):
        pass
    
    def NewLoop(self):
        self.GetActions()
        self.PushList()
    
    def GetActions(self):
        temp = Interface.GetInterfaceActions(self.mousePastLoc)
        self.interactions = temp[0]
        self.mousePastLoc = temp[1]
    
    def PushList(self):
        for i in range(len(self.interactions)):
            aType = Interface.DetermineType(self.interactions[i])
            if aType== 0:
                #window.mouse(interaction))
                #theGUI.mouse(interaction)
                pass
            if aType == 1:
                #if ctrl and ctrl = True
                pass
            if aType == 2:
                #if ctrl and ctrl = False
                pass
            if aType == 3:
                #theSelected.action(interaction)
                #theWindow.action(interaction)
                #theGUI.action(interaction)
                pass
            if aType == 4:
                #theSelected.letter(interaction)
                #theWindow.letter(interaction)
                #theGui.letter(interaction)
                pass
    
def terminate():
    pygame.quit()
    sys.exit()
    
def main():
    powerOverwhelming = Background()
    
    while():
        powerOverwhelming.Draw()
    
if __name__ == '__main__':
    main()
    
        