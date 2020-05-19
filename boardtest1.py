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
        self.move_counter=0
        self.master.title("ConfigChess - (C)2020 Filip Jamroga")       

        self.frame = Frame(self.master) #main container frame
        self.frame.pack()
        
        f_top = Frame(self.frame)
        f_top.pack(side=TOP)
        
        self.canvas = Canvas(self.frame, width=320, height=320)
        self.board = Board(self.canvas)
        self.canvas.bind("<Button-1>", self.callback)
        
        for x in range(0, 8):
            for y in range(0, 8):
                self.board.chart.append((x, y))

        self.l = Label(f_top, text="Player Data Placeholder")
        self.l.pack(side=TOP)
        b2 = Button(f_top, text="Edit Board Shape", command=self.edit1)
        b2.pack(side=LEFT)
        b3 = Button(f_top, text="Edit Piece Placement", command=self.edit2)
        b3.pack(side=LEFT)
        b4 = Button(f_top, text="Edit Miscellanious Options", command=self.edit3)
        b4.pack(side=LEFT)
        b5 = Button(f_top, text="Manage Config", command=self.edit4)
        b5.pack(side=LEFT)
        
        self.bp = Button(self.frame, text="PASS", command=self.passTurn)
        self.bp.pack(side=BOTTOM)
        self.canvas.pack(side=TOP)
        
        self.align(200, 150)
        
        self.redraw(0)
        
    def align(self, x, y):
        self.master.geometry("+{}+{}".format(x, y))
    
    def edit1(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        BoardEdit(x, y, self.board)
        
    def edit2(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        PiecePlaceEdit(x, y, self.board)
        
    def edit3(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        MiscEdit(x, y, self.board, (self.l, self.current_palyer, self.move_counter, self.bp))
    
    def edit4(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        ConfigMgr(x, y, self.board)
    
    def callback(self, event):
        x = event.x//40
        y = event.y//40
        if(self.input_state):#if there is stuff highlighted, try to move, else make a new highlight
            h = self.board.hilite
            if((x, y) in h and (self.board.getPiece(x,y)==None or self.board.getPiece(x,y).team!=self.current_palyer)):
                self.selected_piece.move(x, y)
                if(self.move_counter==self.board.movesPerPlayer):
                    self.move_counter=0
                    if(self.current_palyer == "red"):
                        self.current_palyer = "blue"
                    else:
                        self.current_palyer = "red"
                else:
                    self.move_counter+=1
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
        self.testWin()
        
    
    def testWin(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()        
        if(self.board.winCondition == "All"):
            t = self.board.countTeams()
            if(t["red"]==0 and t["blue"]==0):
                Dialog(x, y, title="GAME OVER", text="Nobody won!", button="Yay?")
                self.master.quit()
            elif(t["red"]==0):
                Dialog(x, y, title="GAME OVER", text="The blue player won!", button="Yay!")
                self.master.quit()
            elif(t["blue"]==0):
                Dialog(x, y, title="GAME OVER", text="The red player won!", button="Yay!")
                self.master.quit()
        elif(self.board.winCondition == "King"):
            if(self.board.countPiece(King(None, None, "red", None)) == 0):
                Dialog(x, y, title="GAME OVER", text="The blue player won!", button="Yay!")
                self.master.quit()
            elif(self.board.countPiece(King(None, None, "blue", None)) == 0):
                Dialog(x, y, title="GAME OVER", text="The red player won!", button="Yay!")
                self.master.quit()
    
    def redraw(self, p):
        self.l.config(text="Player: "+self.current_palyer+" ("+str(self.move_counter)+"/"+str(self.board.movesPerPlayer+1)+")")
        self.l.update()        
        self.board.setHighlight(p)
        self.board.drawBoard(320, 320)
        self.board.drawPieces()
        self.bp.pack_forget()
        if(self.board.passEnable):
            self.bp.pack(side=BOTTOM)
    
    def passTurn(self):
        self.move_counter=0
        if(self.current_palyer == "red"):
            self.current_palyer = "blue"
        else:
            self.current_palyer = "red"
        self.redraw(0)
        
def board(): #init function - call to start
    root = Tk()

    app = BoardApp(root)

    root.mainloop()

board()