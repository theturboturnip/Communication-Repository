#!/usr/bin/env python
import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((600,600))
class character:
    def __init__(self):
        self.x=50
        self.y=50
        self.moveSpeed=1
        self.armLength=30
        self.armThickness=1;
        self.color=(0,0,0)
        self.upArmCoors = []
        self.downArmCoors = []
        self.leftArmCoors = []
        self.rightArmCoors = []
        self.updateArmCoors()
        self.armCoors = self.rightArmCoors

    def updateArmCoors(self):
        self.upArmCoors=   [(self.x-self.armLength/2,self.y-self.armLength),
                            (self.x-self.armLength/2,self.y),
                            (self.x+self.armLength/2,self.y),
                            (self.x+self.armLength/2,self.y-self.armLength)]

        self.downArmCoors= [(self.x-self.armLength/2,self.y+self.armLength),
                            (self.x-self.armLength/2,self.y),
                            (self.x+self.armLength/2,self.y),
                            (self.x+self.armLength/2,self.y+self.armLength)]

        self.rightArmCoors= [(self.x+self.armLength,self.y-self.armLength/2),
                            (self.x,self.y-self.armLength/2),
                            (self.x,self.y+self.armLength/2),
                            (self.x+self.armLength,self.y+self.armLength/2)]

        self.leftArmCoors= [(self.x-self.armLength,self.y-self.armLength/2),
                            (self.x,self.y-self.armLength/2),
                            (self.x,self.y+self.armLength/2),
                            (self.x-self.armLength,self.y+self.armLength/2)]
    def update(self):
        self.move()
        self.updateArmCoors()
        self.draw()
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.armLength/2,0)
        pygame.draw.lines(screen, self.color, False, self.armCoors, self.armThickness)
    def move(self):
        self.x=self.x
class player(character):
    def __init__(self):
        character.__init__(self)
        self.color=(0,0,0)
        
    def move(self):
        pressedButtons=pygame.key.get_pressed()
        if pressedButtons[pygame.K_UP]:
            self.y-=self.moveSpeed
            self.armCoors=self.upArmCoors
        elif pressedButtons[pygame.K_LEFT]:
            self.x-=self.moveSpeed
            self.armCoors=self.leftArmCoors
        elif pressedButtons[pygame.K_DOWN]:
            self.y+=self.moveSpeed
            self.armCoors=self.downArmCoors
        elif pressedButtons[pygame.K_RIGHT]:
            self.x+=self.moveSpeed
            self.armCoors=self.rightArmCoors

class enemy(character):
    def __init__(self):
        character.__init__(self)
        self.color=(255,0,0)
        self.pointsToMoveTo=[[50,150],[100,100]]
        self.x=self.pointsToMoveTo[0][0]
        self.y=self.pointsToMoveTo[0][1]
        self.currentTarget=self.pointsToMoveTo[1]
    def move(self):
        if([self.x,self.y]==self.currentTarget):
            if(self.currentTarget==self.pointsToMoveTo[1]):
                self.currentTarget=self.pointsToMoveTo[0]
            else:
                self.currentTarget=self.pointsToMoveTo[1]
        else:
            if(self.currentTarget[0]!=self.x):
                if(self.currentTarget[0]>self.x):
                    self.x+=self.moveSpeed
                    self.armCoors=self.rightArmCoors
                else:
                    self.x-=self.moveSpeed
                    self.armCoors=self.leftArmCoors
            else:
                if(self.currentTarget[1]>self.y):
                    self.y+=self.moveSpeed
                    self.armCoors=self.downArmCoors
                else:
                    self.y-=self.moveSpeed
                    self.armCoors=self.upArmCoors

def mainLoop():
    newPlayer=player()
    newEnemy=enemy()
    clock=pygame.time.Clock()
    while True:
        msElapsed = clock.tick(60)
        screen.fill((255,255,255))
        newEnemy.update()
        newPlayer.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit(); sys.exit();

mainLoop()
        

