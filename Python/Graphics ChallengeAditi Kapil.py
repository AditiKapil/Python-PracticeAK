#Aditi Kapil
#Graphics Challenge

from tkinter import *
from random import*

#I will need to use Class instead of functions because classes are for specific things. Or just a better way to organise my game
class game:
    def __init__(self):
        self.root=Tk()
        self.RUN=False
        
        self.frame=Frame(bg="lightblue")
        self.frame.pack();
        self.canvas=Canvas(self.frame, bg="purple",width=300,height=300)
        self.canvas.pack()
        self.clock=Label(self.frame, bg="white", fg="black")
        self.clock.pack()
        self.points=Label(self.frame, bg="white", fg="red")
        self.points.pack()
        self.button=Button(self.frame, bg="pink", fg="black", text="Click to start" ,command=self.start)
        self.button.pack()
        
        self.root.mainloop()

    def start(self):
        self.time=0
        self.RUN=True
        
        self.foodX=[]
        self.foodY=[]

        self.trapX=[]
        self.trapY=[]

        self.powerupX=[[],[]]
        self.powerupY=[[],[]]

        self.TEXT="Welcome to tkinter"
        self.point=0
        
        self.x=100
        self.y=100
        self.tempx=100
        self.tempy=100
        self.UP=False
        self.DOWN=False
        self.LEFT=False
        self.RIGHT=False

        self.size=3
        self.canvas.bind("<ButtonPress-1>", self.onMClick)
        self.run()

    def run(self):
        if self.RUN is True:
            self.time+=1
            self.clock['text']="TIME:" + str(self.time//100)
            self.points['text']="Points gathered: " + str(self.point)
            self.move(10*self.size,2)
            self.paint()
            self.root.after(10, self.run)

    def end(self):
        self.RUN=False
        self.canvas.unbind("<ButtonPress-1>")

#The food to help the ball grow
#According to the internet, I need to add "len" in order for the little balls to pop up on the canvas        
    def create_food(self,ball):
        if len(self.foodX) <self.time//1500 +1:
            self.foodX.append(randint(50,250))
        if len(self.foodY) <self.time//1500 +1:
            self.foodY.append(randint(50,250))
        for i in range(0,len(self.foodX)):
            self.canvas.create_rectangle(self.foodX[i], self.foodY[i], self.foodX[i]+10, self.foodY[i]+10, fill="blue")
        for i in range(0,len(self.foodX)):
            if len(self.canvas.find_overlapping(self.foodX[i], self.foodY[i], self.foodX[i]+10, self.foodY[i]+10)) is not 1:
                if ball in self.canvas.find_overlapping(self.foodX[i], self.foodY[i], self.foodX[i]+10, self.foodY[i]+10):
                    self.point+=100
                    self.size+=0.5 
                    self.foodX.pop(i)
                    self.foodY.pop(i)
                    self.create_food(ball)

#The traps that will decrease the size of the ball
#The "len" is also added to the trap balls
    def create_trap(self,ball):
        if len(self.trapX) <self.time//1500 +1:
            self.trapX.append(randint(50,250))
        if len(self.trapY) <self.time//1500 +1:
            self.trapY.append(randint(50,250))
        for i in range(0,len(self.trapX)):    
            self.canvas.create_rectangle(self.trapX[i], self.trapY[i], self.trapX[i]+10, self.trapY[i]+10, fill="red")            
        for i in range(0,len(self.trapX)):
            if len(self.canvas.find_overlapping(self.trapX[i], self.trapY[i], self.trapX[i]+10, self.trapY[i]+10)) is not 1:
                if ball in self.canvas.find_overlapping(self.trapX[i], self.trapY[i], self.trapX[i]+10, self.trapY[i]+10):
                    self.point-=50
                    self.size-=1
                    self.trapX.pop(i)
                    self.trapY.pop(i)
                    self.create_trap(ball)

#Conclusion
        
    def move(self, b,speed):
        if self.UP==True and self.y-b>0:
            self.y-=speed
        elif self.UP==True and self.y-b<=0:
            self.UP=False
            self.DOWN=True
        if self.DOWN==True and self.y+b<300:
            self.y+=speed
        elif self.DOWN==True and self.y+b>=300:
            self.DOWN=False
            self.UP=True
        if self.LEFT==True and self.x-b>0:
            self.x-=speed
        elif self.LEFT==True and self.x-b<=0:
            self.LEFT=False
            self.RIGHT=True
        if self.RIGHT==True and self.x+b<300:
            self.x+=speed
        elif self.RIGHT==True and self.x+b>=300:
            self.RIGHT=False
            self.LEFT=True

    def onMClick(self,event):
        self.tempx=event.x
        self.tempy=event.y
        if event.x> self.x and self.x is not self.tempx :
            self.RIGHT=True
            self.LEFT=False
        elif event.x< self.x and self.x is not self.tempx :
            self.LEFT=True
            self.RIGHT=False
        else:
            self.x=self.tempx    
            self.RIGHT=False
            self.LEFT=False
        if event.y> self.y and self.y is not self.tempy :
            self.DOWN=True
            self.UP=False
        elif event.y< self.y and self.y is not self.tempy :
            self.UP=True
            self.DOWN=False
        else:
            self.y=self.tempy
            self.DOWN=False
            self.UP=False
        

app=game()        
