import random

class Particle:
    def randomize(self):
        self.pos_x=random.randint(0,width)
        self.pos_y=random.randint(0,height)
        self.speed_x=random.randint(-5,5)
        self.speed_y=random.randint(-5,5)
        print(pos_x)
        print(pos_y)
        pass

    def move(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        pass

    def draw_it(self):
       circle(self.pos_x,self.pos_y,10)
       pass
        
def setup():
    size(400,400)
    background(0)
    particles=[]
    for i in range(10):
        parts=Particle()
        particles.append(parts)
    
def draw():
    global particles
    for i in range(len(particles)):
        parts=particles[i]
        parts.draw_it()
        parts.move()
