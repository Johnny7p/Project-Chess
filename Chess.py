# Basic Animation Framework
from tkinter import *
import string
### Splash Screen


#### Move Log Sheet
class LogSheet(object):
    def __init__(self,move,moveCount):
        self.move = move
        self.moveCount = moveCount
        
    def getMove(self,piece,p1,p2):
         
        return 
        
    def drawMove(self,move):
        return
        
#### PLAYER

class Player(object):
    
    def __init__(self,color):
        self.turn = True
        self.color = color
        self.pawns = [Pawn(Position(0,1),color),
                        Pawn(Position(1,1),color),
                        Pawn(Position(2,1),color),
                        Pawn(Position(3,1),color),
                        Pawn(Position(4,1),color),
                        Pawn(Position(5,1),color),
                        Pawn(Position(6,1),color),
                        Pawn(Position(7,1),color)]
        self.rooks = [Rook(Position(0,0),color),
                        Rook(Position(7,0),color)]
        self.knights=[Knight(Position(1,0), color),
                        Knight(Position(6,0), color)]
        self.bishops=[Bishop(Position(2,0), color),
                        Bishop(Position(5,0), color)]
        self.queen = [Queen(Position(3,0),color)]
        self.king  = [King(Position(4,0), color)]
        self.king  = [King(Position(4,0), color)]
                          
    

#### PIECES

class Position(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        


class Pieces(object): 
    def __init__(self,position,color):
        self.Pos = position
        self.color = color
        self.capture = 0
        
        
    def __eq__(self,other):
        return self.type == other
        
        
    def __repr__(self):
        if self.color == 'white':
            return self.type.upper()
        else:
            return self.type.lower()
            
    def isValid(self,Pos2,board):
        p2 = Pos2
        if p2.x < 0 or p2.x > 7 or p2.y < 0 or p2.y > 7:
            return False, 0
        elif board[p2.x][p2.y] == '0':
            return True, 0
        elif board[p2.x][p2.y].color != self.color:# second number def. capture
            return True, 1
        else:
            return False, 0
            
    def move(self,Pos2,board):
        temp = self.Pos
        chessBoard = board
        Game().gameStarted = 1
        tempBoard = board.board
        board.board[Pos2.x][Pos2.y] = chessBoard.board[self.Pos.x][self.Pos.y]
        board.board[self.Pos.x][self.Pos.y] = '0'
        self.Pos = Pos2
        chessBoard.updatedBoard = chessBoard.board
        if self.Pinned(chessBoard.updatedBoard):
            game1.isGameOver()
        chessBoard.updateBoard()
        self.capture = 0
        #LogSheet.getMove(self.Pos,Pos2)
        return chessBoard.board
        
    def Pinned(self,board):
        nColor = board[self.Pos.x][self.Pos.y].color
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '0' and board[row][col].color != nColor:
                    solutions = board[row][col].getPossibleMoves(Position(row,
                    col),board)
                    for coor in solutions:
                        if coor[0] >= 0 and coor[0]<=7 and coor[1]<=7 and\
                         coor[1] >= 0:
                           
                            if (board[coor[0]][coor[1]] == 'k' and \
                            self.color == board[row][col].color) or \
                            (board[coor[0]][coor[1]] == 'K' and \
                            self.color == nColor) :
                                game1.gameOver = True
                                return True
                       
        return False
                        
        
        
        
    
                
class Pawn(Pieces):
    def __init__(self,position,color):
        super().__init__(position,color)
        self.type = "P"
        self.capture = 0
        self.hasMoved = False
        if self.color == 'white':
            self.pImage = PhotoImage(file='./piece_images/WhitePawn.gif')
            self.dir = -1
        else:
            self.pImage  = PhotoImage(file='./piece_images/BlackPawn.gif')
            self.dir = 1
        
            
            
    # Moves up once or twice depedent on if hasMoved
    def getPossibleMoves(self,position,board):
        p = self.Pos = position
        solution = []
        if (p.x == 6 and self.color == "white") or (p.x == 1 and \
        self.color == "black"):
            self.hasMoved = False
        else:
            self.hasMoved = True
        
        for row in range(p.x,p.x + 3*self.dir,self.dir):
            for col in range(p.y - 1,p.y + 2):
                if self.isValid(Position(row,col),board):
                    solution.append((row,col))
        return solution
        
    
    def isValid(self,Pos2,board):
        p2 = Pos2
        if p2.x < 0 or p2.x > 7 or p2.y < 0 or p2.y > 7:
            return False
        if not self.hasMoved:
            if abs(Pos2.x - self.Pos.x) <= 2 and Pos2.y == self.Pos.y:
                if board[Pos2.x][Pos2.y] == '0':
                    return True
            elif (Pos2.x - self.Pos.x)*self.dir == 1 and \
                  abs(Pos2.y - self.Pos.y) == 1 and\
                  board[Pos2.x][Pos2.y] != '0'and \
                  board[Pos2.x][Pos2.y].color != self.color:
                      self.capture = 1
                      return True
        else:
            if abs(Pos2.x - self.Pos.x) <= 1 and Pos2.y == self.Pos.y:
                if board[Pos2.x][Pos2.y] == '0':
                    return True
            elif (Pos2.x - self.Pos.x)*self.dir == 1 and \
                  abs(Pos2.y - self.Pos.y) == 1 and \
                  board[Pos2.x][Pos2.y] != '0'and \
                  board[Pos2.x][Pos2.y].color != self.color:
                      self.capture = 1
                      return True
            else:
                return False
                
    
    def image(self):
        return self.pImage
        
        
        
    
class Rook(Pieces):
    def __init__(self,position,color):
        super().__init__(position,color)
        self.type = "R"
        self.capture = 0
        if self.color == 'white':
            self.pImage = PhotoImage(file = './piece_images/WhiteRook.gif')
        else:
            self.pImage = PhotoImage(file = './piece_images/BlackRook.gif')
    
    
    def image(self):
        return self.pImage
            
            
                
    def getPossibleMoves(self,position,board): #Checks for valid moves vertical
    #and horizontally
        p = self.Pos = position
        solution = []
        dist = 1
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x,p.y+dist),board)
            if x:
                solution.append((p.x,p.y+dist))
                if y == 1:
                    break
            else:
                break
                
           
        for dist in range(1,len(board[p.x])):
            x,y = self.isValid(Position(p.x-dist,p.y),board)
            if x:
                solution.append((p.x-dist,p.y))
                if y == 1:
                    break
                
            else:  
                break
            
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x,p.y-dist),board)
            if x:
                solution.append((p.x,p.y-dist))
                if y == 1:
                    break
            else:  
                break
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x+dist,p.y),board)
            if x:
                solution.append((p.x-dist,p.y))
                if y == 1:
                    break
            else:  
                break
            
            
            
        return solution

        
        
        
    
class Knight(Pieces): #checks for possible moves in L-Shape
    def __init__(self,position,color):
        super().__init__(position,color)
        self.type = "N"
        if self.color == 'white':
            self.pImage = PhotoImage(file='./piece_images/WhiteKnight.gif')
        else:
            self.pImage = PhotoImage(file='./piece_images/BlackKnight.gif')
            
    def isValid(self,position,board):
        return super().isValid(position, board)
    
    def getPossibleMoves(self,position,board):
        p = position
        solution = []
        for row in range(p.x-2,p.x+3):
            for col in range(p.y - 2, p.y + 3):
                if (abs(p.x - row) == 2 and  abs(p.y - col) == 1) or \
                   (abs(p.x - row) == 1 and  abs(p.y - col) == 2):
                       if self.isValid(Position(row,col),board):
                           solution.append((row,col))
        return solution
        

    
    def image(self):
        return self.pImage
        
    
class Bishop(Pieces):
    def __init__(self,position,color):
        super().__init__(position,color)
        self.type = "B"
        self.capture = 0
        if self.color == 'white':
            self.pImage = PhotoImage(file='./piece_images/WhiteBishop.gif')
        else:
            self.pImage = PhotoImage(file='./piece_images/BlackBishop.gif')
        
    #checks for moves in diagonals up to in invalid cell or capture
    def getPossibleMoves(self,position,board):
        p = position
        solution = []
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x+dist,p.y+dist),board)
            if x:
                solution.append((p.x+dist,p.y+dist))
                if y == 1:
                    break
            else:
                break
                
           
        for dist in range(1,len(board[p.x])):
            x,y = self.isValid(Position(p.x-dist,p.y+dist),board)
            if x:
                solution.append((p.x-dist,p.y+dist))
                if y == 1:
                    break
                
            else:  
                break
            
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x+dist,p.y-dist),board)
            if x:
                solution.append((p.x+dist,p.y-dist))
                if y == 1:
                    break
            else:  
                break
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x-dist,p.y-dist),board)
            if x:
                solution.append((p.x-dist,p.y-dist))
                if y == 1:
                    break
            else:  
                break
            
            
        return solution
        
            
    def image(self):
        return self.pImage
    
class Queen(Pieces): 
    def __init__(self,position,color):
        super().__init__(position,color)
        self.type = "Q"
        if self.color == 'white':
            self.pImage = PhotoImage(file='./piece_images/WhiteQueen.gif')
        else:
            self.pImage = PhotoImage(file='./piece_images/BlackQueen.gif')
            
    
    # Checks for possible moves in all directions up to invalid cell or capture
    def getPossibleMoves(self,position,board):
        p = position
        solution = []
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x+dist,p.y+dist),board)
            if x:
                solution.append((p.x+dist,p.y+dist))
                if y == 1:
                    break
            else:
                break
                
           
        for dist in range(1,len(board[p.x])):
            x,y = self.isValid(Position(p.x-dist,p.y+dist),board)
            if x:
                solution.append((p.x-dist,p.y+dist))
                if y == 1:
                    break
                
            else:  
                break
            
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x+dist,p.y-dist),board)
            if x:
                solution.append((p.x+dist,p.y-dist))
                if y == 1:
                    break
            else:  
                break
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x-dist,p.y-dist),board)
            if x:
                solution.append((p.x-dist,p.y-dist))
                if y == 1:
                    break
            else:  
                break
            
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x,p.y+dist),board)
            if x:
                solution.append((p.x,p.y+dist))
                if y == 1:
                    break
            else:
                break
                
           
        for dist in range(1,len(board[p.x])):
            x,y = self.isValid(Position(p.x-dist,p.y),board)
            if x:
                solution.append((p.x-dist,p.y))
                if y == 1:
                    break
                
            else:  
                break
            
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x,p.y-dist),board)
            if x:
                solution.append((p.x,p.y-dist))
                if y == 1:
                    break
            else:  
                break
        for dist in range(1,len(board)):
            x,y = self.isValid(Position(p.x+dist,p.y),board)
            if x:
                solution.append((p.x+dist,p.y))
                if y == 1:
                    break
            else:  
                break
            
                
        return solution
        
    
    def image(self):
        return self.pImage
        
    
class King(Pieces):
    def __init__(self,position,color):
        super().__init__(position,color)
        self.type = "k"
        if self.color == 'white':
            self.pImage = PhotoImage(file='./piece_images/WhiteKing.gif')
        else:
            self.pImage = PhotoImage(file='./piece_images/BlackKing.gif')
            
    def Castle(self,position,board):
        p2 = position
        if p2.x != 4:
            return False
        for dist in range(1,4):
            if self.isValid(p2.x + dist,board):
                continue
            elif board[p2.x + 3][p2.y].type == 'R':
                return True,1
        
        for dist in range(1,5):
            if self.isValid(p2.x - dist,board):
                continue
            elif board[p2.x - 4][p2.y].type == 'R':
                return True,-1
        return False
        
    
    def move(self,position,board):
        super().move(position,board)
        
                
            
        
                 
                 
    def getPossibleMoves(self,position,board):
        p = position
        solution = []
        if self.isValid(Position(p.x,p.y+1),board):
            solution.append((p.x,p.y+1))
        if self.isValid(Position(p.x+1,p.y+1),board):
            solution.append((p.x+1,p.y+1))
        if self.isValid(Position(p.x+1,p.y),board):
            solution.append((p.x+1,p.y))
        if self.isValid(Position(p.x+1,p.y-1),board):
            solution.append((p.x+1,p.y-1))
        if self.isValid(Position(p.x,p.y-1),board):
            solution.append((p.x,p.y-1))
        if self.isValid(Position(p.x-1,p.y-1),board):
            solution.append((p.x-1,p.y-1))
        if self.isValid(Position(p.x-1,p.y),board):
            solution.append((p.x-1,p.y))
        if self.isValid(Position(p.x-1,p.y+1),board):
            solution.append((p.x-1,p.y+1))
        return solution
        
        
    def image(self):
        return self.pImage
####

class Game (object):
    def __init__(self):
        self.gameStarted = 0
        self.gameOver = self.isGameOver()
    
    def newGame(self): return
        
        
    def isGameOver(self): 
        
        return



game1 = Game()
class Board(object):
    
    def __init__(self): 
        self.updatedBoard = 0
        self.board = self.initialize()
        self.selected = []
        self.highlight = []
    
    
    def initialize(self): 
        board = [["0" for j in range(8)] for i in range (8)]
        

        for j in range(8):
            posW = Position(1,j)
            posB = Position(6,j)
            board [6][j] = Pawn(posW,"white")
            board [1][j] = Pawn(posB,"black")

        for i in range(0,8,7):
            if i == 7:
                color = "white"
            else:
                color = "black"
            board [i][0] = Rook(Position(i,0),color)
            board [i][1] = Knight(Position(i,1),color)
            board [i][2] = Bishop(Position(i,2),color)
            board [i][3] = Queen(Position(i,3),color)
            board [i][4] = King(Position(i,4),color)
            board [i][5] = Bishop(Position(i,5),color)
            board [i][6] = Knight(Position(i,6),color)
            board [i][7] = Rook(Position(i,7),color)

            
        return board
        
        

    def updateBoard(self):
        if game1.gameStarted == 0:
            return self.initialize()
        else:
            return self.updatedBoard
            
        
        
    def select(self,row,col): # Selects and highlights possible moves
        self.selected =(row,col)
        self.highlight = []
        moves = self.board[row][col].getPossibleMoves(Position(row,col),
        self.board)
        for move in moves:
            self.highlight.append(move)
            
        return self.selected,self.highlight
            




####################################
# customize these functions
####################################

def init(data):
    data.turn = 0
    data.logo = PhotoImage(file='./piece_images/WhiteKing.gif')
    
    data.screen = 0
    data.selected = 0
    data.highlight = []
    data.board = Board()
    data.moveLogW = 550
    data.boardW = data.width - data.moveLogW - 50
    data.boardH = data.boardW #square board
    data.cellSize = data.boardW / 8
    data.marginY = 100
    data.marginX = 50
    data.boardPos = [data.marginX,data.marginY,data.marginX + data.boardW,
    data.marginY+data.boardH]
    pass

def mousePressed(event, data):
    if data.turn % 2 == 0:
        data.Player = Player('white')
    else:
        data.Player = Player('black')
    if data.screen == 0:
        data.screen += 1
    elif data.screen == 1: 
        if event.y > (data.boardPos[3] ) and \
         event.x > (data.boardPos[2] + 2*data.marginX + 10): #New Game Button
             
             data.board = Board()
             data.turn = 0
             game1.gameStarted = 0
             data.board.updateBoard()
            
            
        for row in range(len(data.board.board)): #Selects and Moves Pieces
            for col in range(len(data.board.board[0])):
                if data.boardPos[1] + (row+1)*data.cellSize > event.y > \
                data.boardPos[1]+row*data.cellSize and \
                data.boardPos[0] + (col+1)*data.cellSize > event.x > \
                data.boardPos[0] +  col*data.cellSize:
                        
                    if data.board.board[row][col] != "0" and \
                    data.board.board[row][col].color == data.Player.color:
                        data.selected,data.highlight=data.board.select(row,col)
                    if (row,col) in data.highlight:
                        data.board.board[data.selected[0]][data.selected[1]]\
                        .move(Position(row,col),data.board)
                        data.turn += 1
                        data.selected = 0
                        data.highlight = []
                    if data.turn % 2 == 0:
                        data.Player = Player('white')
                    else:
                        data.Player = Player('black')
    
    pass

def keyPressed(event, data):    
    # use event.char and event.keysym
    pass

def redrawAll(canvas, data):
    if data.screen == 0:
        drawSplashScreen(data,canvas)
    elif data.screen == 1:
        drawBoard(data,canvas)
        drawLines(data,canvas)
        drawPieces(data, canvas)
        drawHeader(data,canvas)
        drawRestart(data, canvas)
    pass

def drawRestart(data,canvas):
    canvas.create_text(((data.width + data.moveLogW)//2),(data.height - 50),
    text = ("New Game"),font = ("Arial", '30', 'bold'))

def drawHeader(data,canvas):
    canvas.create_text(data.width//2,50,text = (data.Player.color + " to play"),
    font = ("Arial", '30', 'bold italic'))

#Draws Splash Screen
def drawSplashScreen(data,canvas): 
    logo = PhotoImage(file='./piece_images/WhiteKing.gif')
    c = canvas
    c.create_rectangle(0,0,data.width,data.height,fill = 'pink')
    c.create_image(data.width//2,data.height//2,image = data.logo)
    c.create_text(data.width//2,data.height//2 + 100, 
    text = "Click anywhere to Play", font = ('Times', '24', 'bold italic'))
    
def drawBoard(data,canvas):
    c = canvas
    outline = ''
    c.create_rectangle(data.boardPos[0],data.boardPos[1],data.boardPos[2],
    data.boardPos[3],outline = "gray",)
    for row in range(len(data.board.board)):
        #Side Numbers
        digitList = string.digits[::-1]
        numbers = digitList[row+1]
        c.create_text(data.boardPos[0] - 15, 
        data.boardPos[1] + data.cellSize *(row+1) - data.cellSize//2 ,
        text = numbers ,font = ("Times", "15", "bold italic"))
        # Bottom Letters
        letters = string.ascii_uppercase[row]
        c.create_text(data.boardPos[0]+data.cellSize *(row+1)-data.cellSize//2, 
        data.boardPos[3] + 15 ,
        text = letters ,font = ("Times", "15", "bold italic"))

        # Board Colors
        for col in range(len(data.board.board[0])):
            if (row + col) % 2 == 0:
                color = "light blue"
            elif (row + col) % 2 == 1: 
                color = "RoyalBlue4"
                
             
            if (col,row) == data.selected:
                color = 'orange'
            for cell in data.highlight:
            
                if (col,row) == cell:
                    color = 'yellow'
            c.create_rectangle(data.boardPos[0]+row*data.cellSize,
            data.boardPos[1] +  col*data.cellSize,
            data.boardPos[0] + (row+1)*data.cellSize,
            data.boardPos[1] + (col+1)*data.cellSize,
            fill = color)
    
            
    # Log Sheet
    c.create_rectangle(data.boardPos[2] + data.marginX, data.boardPos[1],
    data.width - data.marginX, data.boardPos[3])
    
    
    
                            
                        
    return
    
def drawLines(data,canvas):
    c = canvas
    for line in range(1,8): 
        #Vertical lines
        c.create_line(line*data.cellSize + data.marginX,data.boardPos[1],
        line*data.cellSize + data.marginX,data.boardPos[3])
        #Horizontal Lines
        c.create_line(data.boardPos[0],line*data.cellSize +data.marginY,
        data.boardPos[2],line*data.cellSize + data.marginY)
    return

def drawPieces(data,canvas): #Draws Pieces on Board
    c = canvas
    d = data
    for i in range(len(d.board.board)):
         for j in range(len(d.board.board[0])):
            if data.board.board[i][j] == '0':
                continue
            c.create_image(data.boardPos[0]+j*d.cellSize,
            d.boardPos[1]+i*d.cellSize,
            anchor = NW ,image = d.board.board[i][j].image(),)
            
                 
####################################
# SPLASH SCREEN
####################################
        
    
        
        
    
    
    

####################################
# RUN FUNCTION
####################################
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200,800)
