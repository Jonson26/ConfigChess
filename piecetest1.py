from tkinter import *
import random
from pieces import *

class BoardApp:

    def __init__(self, master):
        self.piece = None
        
        master.title("Simple movement pattern DEMO")

        self.frame = Frame(master) #main container frame
        self.frame.pack()
        
        self.w = Canvas(self.frame, width=100, height=100)
        self.w.pack(side=BOTTOM)

        self.drawBoard()
        self.piece1()
        

    def drawPiece(self, piece): #draw a peg at the given coordinates with the specified colour
        self.w.create_oval(piece.x*20+1, piece.y*20+1, piece.x*20+19, piece.y*20+19, fill="blue")
        
    def drawHighlight(self, c):
        x = c[0]
        y = c[1]
        self.w.create_rectangle(x*20+1, y*20+1, x*20+19, y*20+19, fill="red", outline = "red")
    def drawBoard(self):
        self.w.create_rectangle(0, 0, 100, 100, fill="white")
        i = 0
        while(i<5): #draw horizontal lines
            self.w.create_line(0, i*20, 100, i*20, fill="black")
            i += 1
        i = 0
        while(i<5): #draw vertical lines
            self.w.create_line(i*20, 0, i*20, 100, fill="black")
            i += 1
    
    def piece1(self):
        self.piece = Knight(2, 2, "white")
        for x in self.piece.getMoveTable():
            self.drawHighlight(x)
        self.drawPiece(self.piece)
        
        
def board(): #init function - call to start
    root = Tk()

    app = BoardApp(root)

    root.mainloop()

board()