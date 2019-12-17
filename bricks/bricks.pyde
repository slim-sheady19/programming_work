import random

def setup():
    size(580,500)
    background(14,47,130)

def top_margin():
    fill(0)
    rect(0,0,width,20)
    
def border():
    fill(91,91,92)
    rect(0,20,width,10)
    rect(0,20,10,height)
    rect(width-10,20,height,width)
    
def bricks():
    fill(227,33,11)
    rect(0,0,40,15,7)
    
def powerup():
    fill(255,0,230)
    rect(0,0,40,15,7)
    
def draw():
    top_margin()
    border()
    pushMatrix()
    translate(10,30)
    for i in range(14):
        pushMatrix()
        translate(i*40,0)
        for j in range(8):
            pushMatrix()
            translate(0,j*15)
            if (i + j) % 30 ==0:
                powerup()
            else:
                bricks()
            popMatrix()
        #bricks()
        noLoop()
        popMatrix()
    popMatrix()
    
