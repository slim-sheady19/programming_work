#Shea Galley, Patrick Melancon, Jonathan Wan

import random

x=25
y=550
value=25

def setup():
    size(580,600)
    background(14,47,130)

def draw():
    background(14,47,130)
    top_margin()
    border()
    slider()
    bricks()    

def top_margin():
    fill(0)
    rect(0,0,width,20)
    
def border():
    fill(91,91,92)
    rect(0,20,width,10)
    rect(0,20,10,height)
    rect(width-10,20,height,width)

def bricks():
    pushMatrix()
    translate(10,30)
    for i in range(14):
        pushMatrix()
        translate(i*40,0)
        for j in range(8):
            pushMatrix()
            translate(0,j*15)
            r = random.random()
            if r > 0.99:
                powerup()
            else:
                redbricks()
            #noLoop()
            popMatrix()
        popMatrix()
    popMatrix()

def redbricks():
    fill(227,33,11)
    rect(0,0,40,15,7)
    
def slider():
    global x,y
    if keyPressed:
        if keyCode== LEFT:
            x=x-10
        if keyCode== RIGHT:
            x=x+10
    fill(245,42,15)
    ellipse(x,y+13,25,25)
    ellipse(x+75,y+13,25,25)
    fill(91,91,92)
    rect(x,y,75,25)
    if x < 25:
        x = 25
    if x > 505:
        x = 505
    if mousePressed:
        x=mouseX
    if x < 25:
        x = 25
    if x > 480:
        x = 480
    
def powerup():
    fill(255,0,230)
    rect(0,0,40,15,7)
    
