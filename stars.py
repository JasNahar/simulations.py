import pygame as py
import math
G=100# scaled for screen-space simulation
k=100# scaled for screen-space simulation
c=3e+8
bodies=[]
class Body():
    def __init__(self,x,y,mass,charge,vx,vy,radius):
        bodies.append(self)
        self.mass=mass
        self.charge=charge
        self.radius=radius
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    def distance(self,obj2):
        distance1=math.sqrt((self.x-obj2.x)**2+(self.y-obj2.y)**2)
        if isinstance(obj2,Star):
            if distance1<obj2.radius:
                return None
        return distance1
    def acceleration(self,bodies):
            ax=0
            ay=0
            for i in bodies:
                if i==self:
                    continue
                else:
                    distance1=self.distance(i)
                    if distance1 is None:
                        toremove.append(self)
                        continue
                    else:
                        gravitationalForce=(G*self.mass*i.mass)/distance1**2
                        electrostaticForce=(k*self.charge*i.charge)/distance1**2
                        gravitationalforceX=gravitationalForce*(i.x-self.x)/distance1
                        gravitationalforceY=gravitationalForce*(i.y-self.y)/distance1
                        electrostaticforceX=electrostaticForce*(i.x-self.x)/distance1
                        electrostaticforceY=electrostaticForce*(i.y-self.y)/distance1
                        ax+=(gravitationalforceX/self.mass)+(electrostaticforceX)/self.mass
                        ay+=(gravitationalforceY/self.mass)+(electrostaticforceY)/self.mass
            return ax,ay
    def update(self,dt,accelerations,p):    
        ax,ay=accelerations[p]
        self.x+=self.vx*dt + 0.5*ax*dt**2
        self.y+=self.vy*dt + 0.5*ay*dt**2
        self.vx+=ax*dt
        self.vy+=ay*dt                                  
class Star(Body):
    def __init__(self,x,y,mass,charge,vx,vy):
        radius=max(2*G*mass/c**2,20)
        super().__init__(x,y,mass,charge,vx,vy,radius)     
WIDTH,HEIGHT=1500,800
py.init()
window=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("space")
clock=py.time.Clock()
white=(255,255,255)
darkpurple=(75, 0, 130)
red=(255,0,0)
yellow=(255,255,0)
black=(0,0,0)
toremove=[]
def main():
    run=True
    while run:
        dt=clock.tick(1000)/1000
        for event in py.event.get():
            if event.type==py.QUIT:
                run=False
                break
        accelerations = []
        window.fill(black)
        for body in bodies:
            accelerations.append(body.acceleration(bodies))
        for t in range(len(toremove)):
            bodies.remove(toremove[t])
            del toremove[t]
        for j in  range(len(bodies)):
            bodies[j].update(dt,accelerations,j)
            if isinstance(bodies[j],Star):    
                py.draw.circle(window,white, (bodies[j].x, bodies[j].y), bodies[j].radius)
            else:
                 py.draw.circle(window,yellow, (bodies[j].x, bodies[j].y), bodies[j].radius) 
        py.display.update()
bh = Star(750, 400, 10000, 0, 0, 0)
p1 = Body(750, 200, 1, 0, 50, 0, 5)
p2 = Body(750, 600, 1, 0, -50, 7, 5)
p3 = Body(400, 400, 1, 0, 0, 50, 5)
p4 = Body(1100, 400, 1, 0,0, 45, 5)
p5 = Body(750, 100, 1, 0, 5, 5, 5)  
main()