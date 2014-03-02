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
            type = inputActions[i][0]
            if type == '':
                pass
            elif type == '':
                if self.selected == True:
                    #go through transup
                    pass
            elif type == '':
                if self.selected == True:
                    #go through transdn
                    pass
            elif type == '':
                if self.selected == True:
                    #go through actiondn
                    pass
            elif type == '':
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
 
class Button():
    def __init__(self,pos,offset,rect,image = None,color = Vars.BLACK,outlineColor = Vars.WHITE ,isSwitch = False,switchPos = False):
        #default no image, black bg, white outline, not a switch
        self.pos = pos
        self.offset = offset
        self.rect = rect
        if image != None:
            self.image = self.LoadImage(image)
        else:
            self.image = image
        self.color = color
        self.outlineColor = outlineColor
        self.isSwitch = isSwitch
        self.switchPos = switchPos
        self.size = 5                       #size determines size of bevel
        self.reverse = False
    def LoadImage(self,imageInfo):
        if imageInfo == None:
            return None
        else:
            #DO SHIT HERE
            return None
    
    def DrawImage(self):
        #DO SHIT HERE
        pass
    
    def Draw(self):
        if (self.reverse == True):
            color = self.outlineColor
            outlineColor = self.color
            self.reverse = False
        else:
            color = self.color
            outlineColor = self.outlineColor
        self.DrawBox(self.rect,outlineColor,self.size)
        temp = copy.deepcopy(self.rect)
        temp.topleft = temp.topleft + [2,2]
        temp.inflate_ip(-4,-4)
        self.DrawBox(temp,color,self.size)
        if(self.image != None):
            self.DrawImage()
    
    def DrawBox(self,aRect,color,size):
        main = copy.deepcopy(aRect)
        main.move_ip(size,size)
        sizeNeg = size*-1
        sizeDoubleNeg = 2*sizeNeg
        sizeDouble = 2*size
        main.inflate_ip(sizeDouble,sizeDouble)
        pygame.draw.circle(Vars.DISPLAYSURF,color,main.topleft,size)
        pygame.draw.circle(Vars.DISPLAYSURF,color,main.topright,size)
        pygame.draw.circle(Vars.DISPLAYSURF,color,main.bottomleft,size)
        pygame.draw.circle(Vars.DISPLAYSURF,color,main.bottomright,size)
        pygame.draw.rect(Vars.DISPLAYSURF,color,main)
        temp = main.move(sizeNeg,0)
        pygame.draw.rect(Vars.DISPLAYSURF,color,temp)
        temp = main.move(size,0)
        pygame.draw.rect(Vars.DISPLAYSURF,color,temp)
        temp = main.move(0,size)
        pygame.draw.rect(Vars.DISPLAYSURF,color,temp)        
        temp = main.move(0,sizeNeg)
        pygame.draw.rect(Vars.DISPLAYSURF,color,temp)
        
    def MouseClick(self,aLoc):
        if self.rect.collidepoint(aLoc) == True:
            self.reverse = True
            return True
        return False
    
    def Move(self,diff):
        self.rect.move_ip(diff)
    
class Window():
    def __init__(self, aType, loc, aChild, bgColor = None,borderColor = None,font = None):
        self.type = aType
        self.loc = loc
        self.child = aChild
        self.size = [] #[x,y]; init by type
        self.rects = [] # Whole Window, BG of Child, Titlebar,Right border, Bottom border
        self.titlebarText = [] #text, Surface, Rect; init by type
        self.titlebarBtns = [] #init
        self.bgColor = bgColor
        self.borderColor = borderColor
        self.font = font
        self.mouse = [] # used if window is moving, holds past mouseLoc
        self.moving = False
        self.isSelected = False
        self.childMouse = False
        
        self.Initialize()
    
    def Initialize(self):
        self.InitRects()
    
    def InitRects(self):
        #need to create checking for outside of bounds
        pass            
        
    def Move(self, diff):
        for i in range(len(self.rects)):
            self.rects[1].topleft = self.rects[1].topleft+diff
        self.child.Move(diff)
        for i in range(2):
            self.titlebarBtns[i].Move(diff)
    
    def MouseUp(self, aLoc):
        if self.moving == True:
            self.moving = False
            diffx = aLoc[0]-self.mouse[0]
            diffy = aLoc[1]-self.mouse[1]
            self.Move([diffx,diffy])
        if self.childMouse == True:
            self.childMouse = False
            diffx = aLoc[0]-self.mouse[0]
            diffy = aLoc[1]-self.mouse[1]
            self.child.MouseUp([diffx,diffy])
    
    def MouseMove(self, aLoc):
        if self.moving == True:
            diffx = aLoc[0]-self.mouse[0]
            diffy = aLoc[1]-self.mouse[1]
            self.Move([diffx,diffy])
        if self.childMouse == True:
            diffx = aLoc[0]-self.mouse[0]
            diffy = aLoc[1]-self.mouse[1]
            self.child.MouseMove([diffx,diffy])
    
    def LocColl(self, aLoc):
        #Method is used to check if MouseDown collides with this window
        if self.rects[0].collidepoint(aLoc)==True:
            self.isSelected = True
            #Collide with Child Rect
            if self.rects[1].collidepoint(aLoc)==True:
                self.childMouse = self.child.LocColl(aLoc)
            #Collide with TitleBarRect?
            elif self.rects[2].collidepoint(aLoc) == True:
                for i in range(len(self.titlebarButtons)):
                    if self.titlebarButtons[i].LocColl == True:
                        self.TitlebarBtn(i)
                        return False
                self.moving = True
                self.mouse = aLoc
                return True
            elif self.rects[3].collidepoint(aLoc) == True:
                pass
            elif self.rects[4].collidepoint(aLoc) == True:
                pass
        return False
    
    def TitlebarBtn(self,num):
        if num == 0:
            #esc
            pass
        if num == 1:
            #min
            pass
    
    def Draw(self):
        pygame.draw.rect(Vars.DISPLAYSURF,Vars.DARKGREY,self.rects[0])
        pygame.draw.rect(Vars.DISPLAYSURF,Vars.WHITE,self.rects[1])
        for i in range(2):
            self.titlebarBtns[i].Draw()
        Vars.DISPLAYSURF.blit(self.titlebarText[0],self.titlebarText[1])
        self.child.Draw()
  
class Background():
    def __init__(self):
        self.windows = []
        self.toolButtons = []
        self.toolbarRect = None
        self.titlebarRect = None
        self.startTime = 4
        self.timeSurfs = []
        self.timeRects = []
        self.bgColorRects = []
        self.clockSurf = None
        self.clockRect = None
        self.dateSurf = None
        self.dateRect = None
        self.viewDateInfo = [None,None,None,None,None,None] # MonthSurf/Rect,DaySurf/Rect,YearSurf/Rect
        self.viewDate = [0,0,0]
        
        self.Initialize()
    
    def Initialize(self):
        self.SetTimeRects()
        self.SetBgRects()
        self.UpdateClock()
        self.clockRect = self.clockSurf.get_rect()
        self.clockRect.topleft = Vars.CLOCKPOS
        self.UpdateDate()
        self.dateRect = self.dateSurf.get_rect()
        self.dateRect.topleft = Vars.DATEPOS
        
        timeInfo = list(time.localtime(time.time()))
        self.ChangeViewYear(timeInfo[0])
        self.ChangeViewMonth(timeInfo[1])
        self.ChangeViewDay(timeInfo[2])
        self.viewDateInfo[1] = self.viewMonthSurf.get_rect()
        self.viewDateInfo[1].topleft = Vars.VIEWMONTHPOS
        self.viewDateInfo[3] = self.viewDaySurf.get_rect()
        self.viewDateInfo[3].topleft = self.viewMonthRect.topright
        self.viewDateInfo[5] = self.viewYearSurf.get_rect()
        self.viewDateInfo[5].topleft = self.viewDayRect.topright
        
    def Draw(self):
        self.UpdateClock()
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
        Vars.DISPLAYSURF.blit(self.viewMonthSurf,self.viewMonthRect)
        Vars.DISPLAYSURF.blit(self.viewDaySurf,self.viewDayRect)
        Vars.DISPLAYSURF.blit(self.viewYearSurf,self.viewYearRect)
        Vars.DISPLAYSURF.blit(self.dateSurf,self.dateRect)
        #draw other titlebar elements
        # arrow buttons
     
    def ChangeViewDay(self,aDay):
        self.viewDate[1] = aDay
        if (aDay%10 == 1):
            dayString = aDay + 'st'
        elif (aDay%10 == 2):
            dayString = aDay + 'nd'
        elif (aDay%10 == 3):
            dayString = aDay + 'rd'
        else:
            dayString = aDay + 'th'
        self.viewDateInfo[2] = Vars.CLOCKFONT.render(dayString,True,Vars.BLACK,Vars.TOOLBARGREY)
        
        #when other stuff is implemented do shit
    
    def ChangeViewMonth(self,aMonth):
        self.viewDate[0] = aMonth
        if aMonth == 1:
            monthString = 'January'
        elif aMonth == 2:
            monthString = 'February'
        elif aMonth == 3:
            monthString = 'March'
        elif aMonth == 4:
            monthString = 'April'
        elif aMonth == 5:
            monthString = 'May'
        elif aMonth == 6:
            monthString = 'June'
        elif aMonth == 7:
            monthString = 'July'
        elif aMonth == 8:
            monthString = 'August'
        elif aMonth == 9:
            monthString = 'September'
        elif aMonth == 10:
            monthString = 'October'
        elif aMonth == 11:
            monthString = 'November'
        elif aMonth == 12:
            monthString = 'December'
        self.viewDateInfo[0] = Vars.CLOCKFONT.render(monthString,True,Vars.BLACK,Vars.TOOLBARGREY)
        #when other stuff is implemented do shit
    
    def ChangeViewYear(self,aYear):
        self.viewDate[2] = aYear
        self.viewDateInfo[4] = Vars.CLOCKFONT.render(aYear,True,Vars.BLACK,Vars.TOOLBARGREY)
        #when other stuff is implemented do shit
    
    def UpdateDate(self):
        timeInfo = list(time.localtime(time.time()))
        if timeInfo[1]<10:
            stringDate = '0'+ str(timeInfo[1]) + '/'
        else:
            stringDate = str(timeInfo[1]) + '/'
        if timeInfo[2]<10:
            stringDate = stringDate + '0'+ str(timeInfo[2]) + '/'
        else:
            stringDate = stringDate + str(timeInfo[2]) + '/'
        stringDate = stringDate + str(timeInfo[0])
        
        self.dateSurf = Vars.CLOCKFONT.render(stringDate,True,Vars.BLACK,Vars.TOOLBARGREY)
       
    def UpdateClock(self):
        localTime = time.localtime(time.time())
        timeList = list(localTime)
        if timeList[3] == 0:
            if timeList[4] == 0:
                self.UpdateDate()
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
         
    def Update(self):
        #handle interactions
        self.Draw()
        
def terminate():
    pygame.quit()
    sys.exit()
    
def main():
    powerOverwhelming = Background()
    
    while():
        powerOverwhelming.Update()
    
if __name__ == '__main__':
    main()