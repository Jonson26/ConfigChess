class Piece:
    def __init__(self, x, y, team, board):
        self.x = x
        self.y = y
        self.team = team
        self.board = board
        self.img = None
    
    def getMoveTable(self):
        return []
    
    def getImg(self):
        return self.img
    
    def move(self, x, y):
        if (x, y) in self.getMoveTable():
            op = self.board.getPiece(x, y)
            if(op!=None): #check if there is an other piece on the selected spot
                if(op.team == self.team): #check team of other piece
                    return False
                else:
                    self.board.removepiece(op)
                    self.x = x
                    self.y = y
                    return True
            return False

class Board:
    def __init__(self):
        self.pieces = []
        self.chart = []
        
    def addPiece(self, piece):
        if (piece.x, piece.y) in chart:
            for p in self.pieces:
                if(p.x==piece.x and p.y==piece.y):
                    return False
            self.pieces.append(piece)
            return True
        return False
    
    def getPiece(self, x, y):
        for p in self.pieces:
            if(p.x==x and p.y==y):
                return p
        return None
    
    def removePiece(self, piece):
        if piece in self.pieces:
            i = 0
            while(i<len(self.pieces)):
                if(self.pieces==piece):
                    self.pieces.remove(i)
                    return True
                i+=1
        return False
    
    def getChart(self):
        return self.chart
    