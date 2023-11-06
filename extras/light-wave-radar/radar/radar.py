import tkinter
import math
from enum import Enum

class Radar:

    def __init__(self) -> None:

        self.winHeight = 300
        self.winWidth = 600
        self.refreshInterval = 10

        self.needleAngle = 0
        self.needleSpeed = 10
        self.needleDirection = 1

        self.root = tkinter.Tk()
        self.root.title("Light Wave Radar")

        self.centralizeWindow()

        # create canvas
        self.myCanvas = tkinter.Canvas(self.root, height=300, width=600)
        self.myCanvas.configure(bg='black')
        self.myCanvas.pack(padx=20, pady=20)

    def centralizeWindow(self):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.winWidth/2))
        y_cordinate = int((screen_height/2) - (self.winHeight/2))

        self.root.geometry("{}x{}+{}+{}".format(self.winWidth, self.winHeight, x_cordinate, y_cordinate))

    def drawCircle(self, x, y, radius):
        x = x - (radius/2)
        y = y - (radius/2)
        myCanvas.create_oval(x+radius, y, x, y+radius, fill="white", width=2)

    def drawLine(self, startX, startY, endX, endY, fill, width):
        self.myCanvas.create_line(startX, startY, endX, endY, fill=fill, width=width)

    def clearCanvas(self):
        self.myCanvas.delete('all')

    def getDestination(self, angle, radius= 300):
        x = 300
        y = 300

        angle = (angle+90) * math.pi / 180

        startX = x
        startY = y
        endX   = x + radius * math.sin(angle)
        endY   = y + radius * math.cos(angle)

        return startX, startY, endX, endY

    def drawNeedle(self):
        startX, startY, endX, endY = self.getDestination(self.needleAngle)
        self.drawLine(startX, startY, endX, endY, "red", 3)

    def update(self):

        self.clearCanvas()

        self.drawNeedle()

        self.root.after(self.refreshInterval, self.update)

    def moveNeedle(self):

        self.needleAngle += self.needleDirection

        if self.needleAngle > 180:
            self.needleDirection = -1
        if self.needleAngle < 0:
            self.needleDirection = 1

        self.root.after(self.needleSpeed, self.moveNeedle)



    def show(self):
        self.root.after(self.refreshInterval, self.update)
        self.root.after(self.needleSpeed, self.moveNeedle)
        self.root.mainloop()
