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