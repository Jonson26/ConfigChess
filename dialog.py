from tkinter import Frame, Button, Label, Tk, Canvas, TOP, BOTTOM, LEFT, RIGHT
from abstract import Board
from copy import copy

class Dialog:
    def __init__(self, **args):
        title = args.get("title", None)
        text = args.get("text", None)
        button = args.get("button", None)
        
        root = Tk()
        root.title(title)
        f = Frame(root)
        f.pack()
        Label(f, text=text).pack()
        Button(f, text=button, command=root.quit).pack()
        root.mainloop()
        
class BoardEdit:
    def __init__(self, board):
        self.boardA = board
        self.boardB = copy(board)
        self.root = Tk()
        self.root.title("Board Editing Window") 
        
        f = Frame(self.root)
        f.pack()
        
        b1 = Button(f, text="SAVE", command=self.save)
        b2 = Button(f, text="CANCEL", command=self.root.destroy)
        b1.pack(side=LEFT)
        b2.pack(side=RIGHT)
    
        self.canvas = Canvas(self.root, width=320, height=320)        
        self.boardB.canvas = self.canvas
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack(side=BOTTOM)
        
        self.redraw(0)
        
        root.mainloop()
    
    def save(self):
        self.boardA.chart = copy(self.boardB.chart)
        self.root.destroy()
        
        
    def callback(self, event):
        x = event.x//40
        y = event.y//40
        if((x, y) in self.boardB.chart):
            self.boardB.chart.remove((x, y))
            self.boardB.chart.remove((7-x, 7-y))
        else:
            self.boardB.chart.append((x, y))
            self.boardB.chart.append((7-x, 7-y))
        self.redraw(0)
        
    def redraw(self, p):
        self.boardB.setHighlight(p)
        self.boardB.drawBoard(320, 320)
        self.boardB.drawPieces()