from abstract import Piece
from tkinter import BitmapImage

class Knight(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/knight.xbm")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        return [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
    
class Rook(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/rook.xbm")    
    
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
        self.img = BitmapImage(file="img/bomb"+str(self.timer)+".xbm")
    
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
        self.img = BitmapImage(file="img/bomb"+str(self.timer)+".xbm")
        return super().getImg()
    
    def move(self, x, y):
        self.super().move(x, y)
        timer-=1
        if(timer==0):
            self.board.remove(self)
        return True
