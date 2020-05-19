from tkinter import Frame, Button, Label, Radiobutton, Listbox, Toplevel, Canvas, Entry, Checkbutton, messagebox, ttk, TOP, BOTTOM, LEFT, RIGHT, END, StringVar, BooleanVar
from abstract import Board, BoardConfig
import os as os
import pickle as pickle
from pieces import *
from copy import copy

__piece_types__ = ["Queen", "King", "Rook", "Knight", "Bomb", "Spider", "Bishop", "Pawn"]
__player_colours__ = ["red","blue"]

class Dialog:
    def __init__(self, x, y, **args):
        title = args.get("title", None)
        text = args.get("text", None)
        button = args.get("button", None)
        
        self.root = Toplevel()
        self.root.title(title)
        f = Frame(self.root)
        f.pack()
        Label(f, text=text).pack()
        Button(f, text=button, command=self.root.destroy).pack()
        self.align(x+50, y+50)
        root.mainloop()
    
    def align(self, x, y):
        self.root.geometry("+{}+{}".format(x, y))    
        
class BoardEdit(Dialog):
    def __init__(self, x, y, board):
        self.boardA = board
        self.boardB = copy(board)
        self.boardB.pieces = []
        self.root = Toplevel()
        self.root.title("Board Editing Window") 
        
        f = Frame(self.root)
        f.pack()
        
        b1 = Button(f, text="SAVE", command=self.save)
        b2 = Button(f, text="CANCEL", command=self.root.destroy)
        b3 = Button(f, text="INVERT", command=self.invert)
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=RIGHT)
    
        self.canvas = Canvas(self.root, width=320, height=320)        
        self.boardB.canvas = self.canvas
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack(side=BOTTOM)
        
        self.redraw(0)
        
        self.align(x, y)
        
        self.root.mainloop()  
    
    def save(self):
        self.boardA.chart = copy(self.boardB.chart)
        self.boardA.pieces = copy(self.boardB.pieces)
        self.boardA.setHighlight(0)
        self.boardA.drawBoard(320, 320)
        self.boardA.drawPieces()
        self.root.destroy()
    
    def invert(self):
        for x in range(0, 8):
            for y in range(0, 8):
                if((x, y) in self.boardB.chart):
                    self.boardB.chart.remove((x, y))
                else:
                    self.boardB.chart.append((x, y))
        self.redraw(0)
        
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
        
class PiecePlaceEdit(BoardEdit):
    def __init__(self, x, y, board):
        self.boardA = board
        self.boardB = copy(board)
        self.root = Toplevel()
        self.root.title("Piece Placement Editing Window") 
        
        f1 = Frame(self.root) #frame containing the save and cancel buttons
        f1.pack(side=TOP)
        
        f2 = Frame(self.root) #frame containing piece selection
        f2.pack(side=LEFT)
        
        b1 = Button(f1, text="SAVE", command=self.save)
        b2 = Button(f1, text="CANCEL", command=self.root.destroy)
        b1.pack(side=LEFT)
        b2.pack(side=RIGHT)
        
        l1 = Label(f2, text="Type")
        l2 = Label(f2, text="Colour")
        
        self.c1 = ttk.Combobox(f2, values=__piece_types__) #menu for piece type selection
        self.c1.current(0)
        
        l1.pack()
        self.c1.pack()
        l2.pack()
        
        self.v1 = StringVar() #radiobuttons for piece colour selection
        self.v1.set("red")
        for c in __player_colours__:
            b = Radiobutton(f2, text=c, variable=self.v1, value=c)
            b.pack()
            
        self.v2 = BooleanVar()
        c = Checkbutton(f2, text="Centrally Symmetrical Opponent", variable=self.v2)
        self.v2.set(False)
        c.pack()
    
        self.canvas = Canvas(self.root, width=320, height=320)        
        self.boardB.canvas = self.canvas
        self.canvas.bind("<Button-1>", self.callback1)
        self.canvas.bind("<Button-3>", self.callback2)
        self.canvas.pack(side=BOTTOM)
        
        self.redraw(0)
        
        self.align(x, y)
        
        self.root.mainloop()
        
    def place(self, x, y, t, c):
        p = None
        if(self.boardB.getPiece(x, y)==None):
            if(t=="Rook"):
                p=Rook(x, y, c, self.boardA)
            if(t=="Knight"):
                p=Knight(x, y, c, self.boardA)
            if(t=="Bomb"):
                p=Bomb(x, y, c, self.boardA)
            if(t=="Queen"):
                p=Queen(x, y, c, self.boardA)
            if(t=="King"):
                p=King(x, y, c, self.boardA)
            if(t=="Spider"):
                p=Spider(x, y, c, self.boardA)
            if(t=="Bishop"):
                p=Bishop(x, y, c, self.boardA)
            if(t=="Pawn"):
                p=Pawn(x, y, c, self.boardA)
            if(p!=None):
                self.boardB.addPiece(p)        
    
    def callback1(self, event):
        x = event.x//40
        y = event.y//40
        t = self.c1.get()
        c = self.v1.get()
        
        self.place(x, y, t, c)
        
        if(self.v2.get()):
            if(c=="red"):
                c="blue"
            else:
                c="red"
            x=7-x
            y=7-y
            
            self.place(x, y, t, c)           
        self.redraw(0)
        
    def callback2(self, event):
        x = event.x//40
        y = event.y//40
        self.boardB.removePiece(self.boardB.getPiece(x, y))
        if(self.v2.get()):
            self.boardB.removePiece(self.boardB.getPiece(7-x, 7-y))
        self.redraw(0)
        
class MiscEdit(Dialog):
    def __init__(self, x, y, board, playerdata):
        self.pd = playerdata
        self.board = board
        self.root = Toplevel()
        self.root.title("Miscellanious Gameplay Options Editing Window") 
        
        f1 = Frame(self.root)
        f1.pack(side=TOP)
        f2 = Frame(self.root)
        f2.pack(side=TOP)   
        f3 = Frame(self.root)
        f3.pack(side=TOP)        
        
        b1 = Button(f1, text="SAVE", command=self.save)
        b2 = Button(f1, text="CANCEL", command=self.root.destroy)
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        
        l1 = Label(f2, text="Maximum amount of moves per player per turn: ")
        self.l2 = Label(self.root, text = " ")
        
        self.e = Entry(f2)
        self.e.delete(0, END)
        self.e.insert(0, self.board.movesPerPlayer+1) 
        
        l1.pack(side=LEFT)
        self.e.pack(side=LEFT)
        self.l2.pack(side=BOTTOM)

        l3 = Label(f3, text="Win condition:")
        
        self.c1 = ttk.Combobox(f3, values=["Until one player loses all of his pieces", "Until one of the opponents has no more Kings"], width=50) #menu for win condition selection
        if(self.board.winCondition == "All"):
            self.c1.current(0)
        elif(self.board.winCondition == "King"):
            self.c1.current(1)
        
        l3.pack(side=LEFT)
        self.c1.pack(side=LEFT)
        
        self.v2 = BooleanVar()
        c = Checkbutton(f3, text="Enable Turn Pass", variable=self.v2)
        self.v2.set(self.board.passEnable)
        c.pack(side=BOTTOM)        

        self.align(x, y)        
        self.root.mainloop()
    
    def save(self):
        try:
            i = int(self.e.get())
            if(i>0):
                self.board.movesPerPlayer = i-1
                c = self.c1.current()
                self.board.passEnable = self.v2.get()
                self.pd[0].config(text="Player: "+self.pd[1]+" ("+str(self.pd[2])+"/"+str(i)+")")
                self.pd[0].update()
                self.pd[3].pack_forget()
                if(self.v2.get()):
                    self.pd[3].pack(side=BOTTOM)
                self.root.destroy()
                if(c==0):
                    self.board.winCondition = "All"
                elif(c==1):
                    self.board.winCondition = "King"
            else:
                self.l2.configure(text="Error: invalid value! Try again with a different value or give up")
                self.l2.pack(side=BOTTOM)
        except:
            self.l2.config(text="Error: invalid value! Try again with a different value or give up")
            self.l2.update()
    
class ConfigMgr(Dialog):
    def __init__(self, x, y, board):
        self.root = Toplevel()
        self.root.title("Config Manager")
        
        self.board = board

        f1 = Frame(self.root)
        f2 = Frame(self.root)
        f3 = Frame(f2)
        f1.pack(side=LEFT)
        f2.pack(side=LEFT)
        f3.pack(side=TOP)

        self.listbox = Listbox(f1)        
        self.files = []
        self.loadFileList()
        self.listbox.pack()
        
        l1 = Label(f3, text="new File name:")
        l1.pack(side=LEFT)
        
        self.e = Entry(f3)
        self.e.delete(0, END)
        self.e.insert(0, "FILENAME")
        self.e.pack(side=LEFT)
        
        buttons = []
        buttons.append(Button(f2, text = "Save to selected", command=self.saveConf))
        buttons.append(Button(f2, text = "Save to new File", command=self.newConf))
        buttons.append(Button(f2, text = "Load selected File", command=self.loadConf))
        buttons.append(Button(f2, text = "Delete selected File", command=self.delConf))
        buttons.append(Button(f2, text = "Continue", command=self.root.destroy))
        for b in buttons:
            b.pack(side=TOP)
        
        self.align(x, y)
        self.root.mainloop()
    
    def loadFileList(self):
        if(not os.path.exists("./CONF")):
            os.mkdir("./CONF")
        self.files = os.listdir("./CONF/")
        self.listbox.delete(0, END)
        for item in self.files:
            self.listbox.insert(END, item)
        self.listbox.selection_set(0)
        self.listbox.update()
    
    def saveConf(self):
        f = open(self.listbox.selection_get(), "wb")
        data = BoardConfig(copy(self.board))
        data_b = pickle.dumps(data)
        f.write(data_b)
        f.close()
        self.loadConf()
    
    def newConf(self):
        f = open("./CONF/"+self.e.get(), "wb")
        data = BoardConfig(copy(self.board))
        data_b = pickle.dumps(data)
        f.write(data_b)
        f.close()
        self.loadFileList()
        print(self.files)
        f = open("./CONF/"+self.e.get(), "rb")
        data_b = f.read()
        data = pickle.loads(data_b)
        data.load(self.board)
        f.close()
        self.redraw(0)
    
    def loadConf(self):
        f = open("./CONF/"+self.listbox.selection_get(), "rb")
        data_b = f.read()
        data = pickle.loads(data_b)
        data.load(self.board)
        f.close()
        self.redraw(0)
    
    def delConf(self):
        MsgBox = messagebox.askquestion('WARNING','Are you sure you want to delete this file?',icon = 'warning')
        if(MsgBox=="yes"):
            os.remove("./CONF/"+self.listbox.selection_get())
            self.loadFileList()
        self.root.lift()
    
    def redraw(self, p):
        self.board.setHighlight(p)
        self.board.drawBoard(320, 320)
        self.board.drawPieces()    