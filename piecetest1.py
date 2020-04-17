from tkinter import *

from abstract import *
from pieces import *

import random

class BoardApp:

    def __init__(self, master):
        self.piece = None
        
        master.title("Simple movement pattern DEMO")

        self.frame = Frame(master) #main container frame
        self.frame.pack()
        
        f1 = Frame(self.frame)
        f1.pack(side = TOP)
        
        b1 = Button(f1, text="Knight", command=self.piece1)
        b2 = Button(f1, text="Rook", command=self.piece2)
        b3 = Button(f1, text="Bomb", command=self.piece3)     
        b1.pack(side = LEFT)
        b2.pack(side = LEFT)
        b3.pack(side = LEFT)
        

        l1 = Label(f1, text="n=")
        self.e1 = Entry(f1)
        l1.pack(side=LEFT)
        self.e1.pack(side=LEFT)
        
        self.w = Canvas(self.frame, width=220, height=220)
        self.w.pack(side=BOTTOM)
        
        self.drawBoard()        

    def drawPiece(self, piece): #draw a peg at the given coordinates with the specified colour
        img=piece.getImg()
        self.w.create_image(piece.x*20+1, piece.y*20+1, anchor=NW, image=img)
        
    def drawHighlight(self, c):
        x = c[0]
        y = c[1]
        self.w.create_rectangle(x*20+1, y*20+1, x*20+19, y*20+19, fill="red", outline = "red")
        
    def drawBoard(self):
        self.w.create_rectangle(0, 0, 220, 220, fill="white")
        i = 0
        while(i<11): #draw horizontal lines
            self.w.create_line(0, i*20, 220, i*20, fill="black")
            i += 1
        i = 0
        while(i<11): #draw vertical lines
            self.w.create_line(i*20, 0, i*20, 220, fill="black")
            i += 1
    
    def piece1(self):
        self.drawBoard()
        self.piece = Knight(5, 5, "white", Board())
        for x in self.piece.getMoveTable():
            self.drawHighlight(x)
        self.drawPiece(self.piece)
        
    def piece2(self):
        self.drawBoard()
        self.piece = Rook(5, 5, "white", Board())
        for x in self.piece.getMoveTable():
            self.drawHighlight(x)
        self.drawPiece(self.piece)
        
    def piece3(self):
        try:
            n = int(self.e1.get())
        except:
            n = 5
        if(n>5 or n<1):
            n = 5
        self.drawBoard()
        self.piece = Bomb(5, 5, "white", Board())
        self.piece.timer = n
        for x in self.piece.getMoveTable():
            self.drawHighlight(x)
        self.drawPiece(self.piece)        
        
        
def board(): #init function - call to start
    root = Tk()

    app = BoardApp(root)

    root.mainloop()

board()