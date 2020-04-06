from abstract import Piece
from tkinter import PhotoImage

class Knight(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = PhotoImage(file="img/knight.gif")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        return [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
    
class Rook(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = PhotoImage(file="img/rook.gif")    
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = []
        for i in range(-10, 10):
            if(0!=i):
                t.append((x + i, y))
        for i in range(-10, 10):
            if(0!=i):
                t.append((x, y + i))
        return t    
    
class Bomb(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)   
        self.timer=5
        self.img = PhotoImage(file="img/bomb"+str(self.timer)+".gif")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = []
        for i in range(-10, 10):
            if(0!=i):
                t.append((x + i, y))
        for i in range(-10, 10):
            if(0!=i):
                t.append((x, y + i))
        for i in range(-10, 10):
            if(0!=i):
                t.append((x + i, y - i))
                t.append((x + i, y + i))
        return t
    
    def getImg(self):
        self.img = PhotoImage(file="img/bomb"+str(self.timer)+".gif")
        return self.img
    
    def move(self, x, y):
        self.super().move(x, y)
        timer-=1
        if(timer==0):
            self.board.remove(self)
        return True
