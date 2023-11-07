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

    def drawRadar(self):

        pad = 20
        x = 400

        width = 50
        height = 50
        cx = self.winWidth / 2
        cy = self.winHeight

        self.drawRec(cx-width/2, cy-height, width+(cx-width/2), cy)
        # self.drawArc(cx, 0, 200, 200)


        # for dist in range(0, x, 20):
        # coord = 50, 50, (275*2), (300*2)
        # # coord = 5+pad, 5+pad, 300*2-pad, 300*2-pad
        # self.myCanvas.create_arc(coord, start=0, extent=180, fill="#2E6B6F", style=tkinter.CHORD)

        # coord = 150, 150, 600,
        # # coord = 5+pad, 5+pad, 300*2-pad, 300*2-pad
        # self.myCanvas.create_arc(coord, start=0, extent=180, fill="#2E6B6F", width=2)

        # draw arcs
        # for dist in range(0, x, 20):
        #     self.myCanvas.create_arc(dist+20, dist+20, (x*2)-dist-10, (x*2)-dist-10, start=0, extent=180, fill="#2E6B6F")

        # for x in range(0, 180, 20):
        #     startX, startY, endX, endY = self.getDestination(x)
        #     self.drawLine(startX, startY, endX, endY, "white", 1)

    def drawArc(self, x0, y0, x1, y1):
        self.myCanvas.create_arc(x0, y0, x1, y1, start=0, width=0, extent=180, fill="#2E6B6F", style=tkinter.CHORD)

    def drawCircle(self, x, y, radius):
        x = x - (radius/2)
        y = y - (radius/2)
        self.myCanvas.create_oval(x+radius, y, x, y+radius, fill="white", width=2)

    def drawLine(self, startX, startY, endX, endY, fill, width):
        self.myCanvas.create_line(startX, startY, endX, endY, fill=fill, width=width)

    def drawRec(self, x0, y0, x1, y1):
        self.myCanvas.create_rectangle(x0, y0, x1, y1, fill="blue", outline = 'blue')

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

        self.drawRadar()

        # self.drawNeedle()

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
