from abstract import *
from pieces import *
from tkinter import *   
from random import randint
    
class BoardApp:

    def __init__(self, master):
        master.title("Simple bard drawing DEMO")

        self.frame = Frame(master) #main container frame
        self.frame.pack()

        
        b = Button(self.frame, text="generate", command=self.generate)
        b.pack()
        
        self.canvas = Canvas(self.frame, width=320, height=320)        
        self.board = Board(self.canvas)
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack(side=BOTTOM)  
        
        t = []
        for x in range(0,8):
            for y in range(0,8):
                t.append((x,y))
        self.board.chart = t
        
        self.generate()       
        
    def generate(self):
        t = ["white", "black"]
        for p in self.board.pieces:
            self.board.pieces = []
        for x in range(0,10):
            x = randint(0,2)
            if(x==0):
                p = Knight(randint(0,7), randint(0,7), t[randint(0,1)], self.board)
            elif(x==1):
                p = Rook(randint(0,7), randint(0,7), t[randint(0,1)], self.board)
            elif(x==2):
                p = Bomb(randint(0,7), randint(0,7), t[randint(0,1)], self.board)
                p.timer = randint(1,5)
            self.board.addPiece(p) 
        self.board.setHighlight(0)
        self.board.drawBoard(320, 320)
        self.board.drawPieces()
        
    def callback(self, event):
        x = event.x//40
        y = event.y//40
        print("clicked at", event.x, event.y, "|", x, y) 
        p = self.board.getPiece(x, y)
        if(p!=None):
            self.board.setHighlight(p)
            self.board.drawBoard(320, 320)
            self.board.drawPieces()            
        else:
            self.board.setHighlight(0)
            self.board.drawBoard(320, 320)
            self.board.drawPieces()            
        
        
def board(): #init function - call to start
    root = Tk()

    app = BoardApp(root)

    root.mainloop()

board()