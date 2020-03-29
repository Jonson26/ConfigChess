from abstract import Piece

class Knight(Piece):
    
    def getMoveTable(self):
        x = self.x
        y = self.y
        return [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
    
class Rook(Piece):
    
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