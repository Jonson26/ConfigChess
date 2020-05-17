from abstract import Piece
from tkinter import BitmapImage

class Knight(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/knight.xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/knight.xbm")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        return [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
    
class Rook(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/rook.xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/rook.xbm")
    
    def getMoveTable(self):
        t = []
        t += self.genLine(1, 1, 0)
        t += self.genLine(1, 0, 1)
        t += self.genLine(-1, 1, 0)
        t += self.genLine(-1, 0, 1)
        return t
   
class Bomb(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)   
        self.timer=5
        self.img = BitmapImage(file="img/bomb"+str(self.timer)+".xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/bomb"+str(self.timer)+".xbm")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = []
        t += self.genLine(1, 1, 0)
        t += self.genLine(1, 1, 1)
        t += self.genLine(1, 0, 1)
        t += self.genLine(1, -1, 1)
        t += self.genLine(1, -1, 0)
        t += self.genLine(1, -1, -1)
        t += self.genLine(1, 0, -1)
        t += self.genLine(1, 1, -1)
        return t
    
    def getImg(self):
        self.img = BitmapImage(file="img/bomb"+str(self.timer)+".xbm")
        return super().getImg()
    
    def move(self, x, y):
        super().move(x, y)
        self.timer-=1
        if(self.timer==0):
            self.board.removePiece(self)
        return True

class Queen(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/queen.xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/queen.xbm")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = []
        t += self.genLine(1, 1, 0)
        t += self.genLine(1, 1, 1)
        t += self.genLine(1, 0, 1)
        t += self.genLine(1, -1, 1)
        t += self.genLine(1, -1, 0)
        t += self.genLine(1, -1, -1)
        t += self.genLine(1, 0, -1)
        t += self.genLine(1, 1, -1)
        return t
    
class King(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/king.xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/king.xbm")    
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                t.append((x+i, y+j))
        return t
    
class Spider(Piece):
    
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/spider.xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/spider.xbm")    
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = [(x-2, y), (x-1, y+1), (x, y+2), (x+1, y+1), (x+2, y), (x+1, y-1), (x, y-2), (x-1, y-1)]
        return t

class Bishop(Piece):
    def __init__(self, x, y, team, board):
        super().__init__(x, y, team, board)
        self.img = BitmapImage(file="img/bishop.xbm")
    
    def reloadImg(self):
        self.img = BitmapImage(file="img/bishop.xbm")
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        t = []
        t += self.genLine(1, 1, 1)
        t += self.genLine(1, -1, 1)
        t += self.genLine(1, -1, -1)
        t += self.genLine(1, 1, -1)
        return t
    