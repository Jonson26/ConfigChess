from tkinter import NW

black_piece = "blue"
white_piece = "red"
black_tile = "black"
white_tile = "white"

hilite_color = "green"
tile_size = 40

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
        if((self.x+self.y)%2==1):
            self.img.config(background=black_tile)
        else:
            self.img.config(background=white_tile)
            
        if(self.team=="red"):
            self.img.config(foreground=white_piece)
        else:
            self.img.config(foreground=black_piece)
        return self.img
    
    def move(self, x, y):
        if (x, y) in self.getMoveTable():
            op = self.board.getPiece(x, y)
            if(op==None): #check if there is an other piece on the selected spot
                self.x = x
                self.y = y
                return True                
            elif(op.team == self.team): #check team of other piece
                return False
            else:
                self.board.removePiece(op)
                self.x = x
                self.y = y
                return True
            
            return False

class Board:
    def __init__(self, canvas):
        self.pieces = []
        self.chart = []
        self.hilite = []
        self.canvas = canvas
        
    def addPiece(self, piece):
        if (piece.x, piece.y) in self.chart:
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
            self.pieces.remove(piece)
            return True
        return False
    
    def getChart(self):
        return self.chart
    
    def drawBoard(self, width, height):
        self.canvas.create_rectangle(0, 0, width, height, fill="grey")
        
        for x in self.chart:
            if((x[0]+x[1])%2==1):
                f = black_tile
            else:
                f = white_tile
            self.canvas.create_rectangle(x[0]*tile_size, x[1]*tile_size, (x[0]+1)*tile_size, (x[1]+1)*tile_size, fill=f)
    
        for h in self.hilite:
            self.canvas.create_rectangle(h[0]*tile_size, h[1]*tile_size, (h[0]+1)*tile_size-1, (h[1]+1)*tile_size-1, fill=hilite_color)        
    
    def drawPieces(self): #draw a piece at the given coordinates with the specified colour
        for piece in self.pieces:
            img = piece.getImg()
            if((piece.x, piece.y) in self.hilite):
                img.config(background=hilite_color)
            self.canvas.create_image(piece.x*tile_size+1, piece.y*tile_size+1, anchor=NW, image=img) 
    
    def setHighlight(self, piece):
        if(piece==0):
            self.hilite = []
        else:
            h = piece.getMoveTable()
            t = []
            for x in h:
                if(x in self.chart):
                    t.append(x)
            h = t
            self.hilite = h
            
    def countTeams(self):
        t = {
            "red": 0,
            "blue": 0
        }
        for p in self.pieces:
            t[p.team]+=1
        return t