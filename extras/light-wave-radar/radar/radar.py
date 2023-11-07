import tkinter
import math
from enum import Enum

class Radar:

    def __init__(self) -> None:

        self.events = {}
        self.winHeight = 300
        self.winWidth = 600

        self.radarSize = 500

        self.refreshInterval = 10

        self.needleAngle = 45
        self.needleSpeed = 10
        self.needleDirection = 1

        self.root = tkinter.Tk()
        self.root.title("Light Wave Radar")

        self.centralizeWindow()

        # create canvas
        canvasHeight = 300
        canvasWidth = 600
        self.myCanvas = tkinter.Canvas(self.root, height=canvasHeight, width=canvasWidth)
        self.myCanvas.configure(bg='black')

        self.myCanvas.pack()
        # self.myCanvas.pack(fill="both", expand=True)

    def centralizeWindow(self):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.winWidth/2))
        y_cordinate = int((screen_height/2) - (self.winHeight/2))

        # self.root.geometry("{}x{}+{}+{}".format(self.winWidth+20, self.winHeight+20, x_cordinate, y_cordinate))
        self.root.geometry("{}x{}".format(self.winWidth+20, self.winHeight+20))

    def getBottomDimensions(self):
        cx = self.winWidth / 2
        cy = self.winHeight - 20
        return cx, cy

    def getDestination(self, x, y, angle, radius):

        angle = (angle+90) * math.pi / 180

        endX   = x + radius * math.sin(angle)
        endY   = y + radius * math.cos(angle)

        return endX, endY

    def drawRadar(self):

        for x in range(self.radarSize, 0, -100):
            self.drawArcFromBottom(x, x)

        for x in range(0, 180+1, 30):
            self.drawLineFromBottom(x, self.radarSize / 2, "white", 1)
            self.drawTextFromBottom(x, self.radarSize / 2, str(x)+u"\u00b0")

    def drawArc(self, x0, y0, x1, y1):
        self.myCanvas.create_arc(x0, y0, x1, y1, start=0, width=0, extent=180, fill="#2E6B6F", style=tkinter.CHORD)

    def drawCircle(self, x, y, radius):
        x = x - (radius/2)
        y = y - (radius/2)
        self.myCanvas.create_oval(x+radius, y, x, y+radius, fill="white", width=2)

    def drawLine(self, startX, startY, endX, endY, fill="red", width=1):
        self.myCanvas.create_line(startX, startY, endX, endY, fill=fill, width=width)

    def drawRec(self, x0, y0, x1, y1):
        self.myCanvas.create_rectangle(x0, y0, x1, y1, fill="blue", outline = 'red')

    def drawText(self, x=10, y=10, text="", angle=0, font="Times 10"):
        self.myCanvas.create_text(x, y, fill="white", font=font, text=text, angle=angle)

    def drawArcFromBottom(self, width, height):

        cx, cy = self.getBottomDimensions()

        self.drawArc(cx-width/2, cy-height/2, width+(cx-width/2), cy+height/2)

    def drawRecFromBottom(self, width=50, height=50):

        cx, cy = self.getBottomDimensions()

        self.drawRec(cx-width/2, cy-height, width+(cx-width/2), cy)

    def drawLineFromBottom(self, angle, radius, fill="red", width=1):

        cx, cy = self.getBottomDimensions()

        endX, endY = self.getDestination(cx, cy, angle, radius)

        self.drawLine(cx, cy, endX, endY, fill, width)

    def drawTextFromBottom(self, angle, radius, text):

        cx, cy = self.getBottomDimensions()

        endX, endY = self.getDestination(cx, cy, angle, radius+10)

        self.drawText(endX, endY, text, 0-(90-angle))

    def clearCanvas(self):
        self.myCanvas.delete('all')

    def drawNeedle(self):
        self.drawLineFromBottom(self.needleAngle, self.radarSize / 2)

    def update(self):

        self.clearCanvas()

        self.drawRadar()

        self.drawNeedle()

        self.root.after(self.refreshInterval, self.update)

    def moveNeedle(self):

        self.needleAngle += self.needleDirection

        self.trigger("needleMoved", self.needleAngle)

        if self.needleAngle >= 180:
            self.needleDirection = -1
        if self.needleAngle <= 0:
            self.needleDirection = 1

        self.root.after(self.needleSpeed, self.moveNeedle)

    def show(self):
        self.root.after(self.refreshInterval, self.update)
        self.root.after(self.needleSpeed, self.moveNeedle)
        self.root.mainloop()

    def on(self, eventName, callback):

        if not eventName in self.events.keys():
            self.events[eventName] = []

        self.events[eventName].append(callback)

    def trigger(self, eventName, args):
        for callback in self.events[eventName]:
            callback(args)
