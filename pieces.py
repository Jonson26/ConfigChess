class Piece:
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        self.status = True #True- alive, False - beaten
    
    def getMoveTable(self):
        return []
    
    def move(self, x, y):
        if (x, y) in self.getMoveTable():
            otherpiece = False
            if(otherpiece): #check if there is an other piece on the selected spot
                if(otherpieceteam == self.team): #check team of other piece
                    return False
                else:
                    #beat the other
                    self.x = x
                    self.y = y
                    return True
            return False

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