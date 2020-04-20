from abstract import *
from pieces import *
from tkinter import *   
from random import randint
from dialog import *
    
class BoardApp:

    def __init__(self, master):
        self.master=master
        self.input_state = False #False: waiting for piece selection; True: waiting for move selection
        self.selected_piece = None
        self.current_palyer="red" #red vs blue
        master.title("Simple board drawing DEMO")

        self.frame = Frame(self.master) #main container frame
        self.frame.pack()

        self.l = Label(self.frame, text=self.current_palyer)
        self.l.pack()
        b1 = Button(self.frame, text="generate", command=self.generate)
        b1.pack()
        b2 = Button(self.frame, text="edit", command=self.edit)
        b2.pack()
        
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
        
    def edit(self):
        b = BoardEdit(self.board)
        
    def generate(self):
        t = ["red", "blue"]
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
        if(self.input_state):
            h = self.board.hilite
            if((x, y) in h and (self.board.getPiece(x,y)==None or self.board.getPiece(x,y).team!=self.current_palyer)):
                self.selected_piece.move(x, y)
                if(self.current_palyer == "red"):
                    self.current_palyer = "blue"
                else:
                    self.current_palyer = "red"
                self.l.config(text=self.current_palyer)
                self.l.update()
            self.redraw(0)
            self.input_state = False
        else:
            self.selected_piece = self.board.getPiece(x, y)            
            if(self.selected_piece!=None and self.selected_piece.team == self.current_palyer):
                self.redraw(self.selected_piece)
                self.input_state = True
            else:
                self.redraw(0)
                self.input_state = False
        t = self.board.countTeams()
        if(t["red"]==0 and t["blue"]==0):
            Dialog(title="GAME OVER", text="Nobody won!", button="Yay?")
            self.master.quit()
        elif(t["red"]==0):
            Dialog(title="GAME OVER", text="The blue player won!", button="Yay!")
            self.master.quit()
        elif(t["blue"]==0):
            Dialog(title="GAME OVER", text="The red player won!", button="Yay!")
            self.master.quit()
    
    def redraw(self, p):
        self.board.setHighlight(p)
        self.board.drawBoard(320, 320)
        self.board.drawPieces()        
        
def board(): #init function - call to start
    root = Tk()

    app = BoardApp(root)

    root.mainloop()

board()