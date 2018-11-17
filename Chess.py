# Basic Animation Framework
from tkinter import *


class Game (object):
    def __init__(self):
        self.gameOver = isGameOver()
    
    def newGame(self): return
        
        
    def isGameOver(self): return
        

    
####################################
# customize these functions
####################################

def init(data):
    data.board = [[0]*8]*8
    data.moveLogW = 550
    data.boardW = data.width - data.moveLogW - 50
    data.boardH = data.boardW #square board
    data.cellSize = data.boardW / 8
    data.marginY = 100
    data.marginX = 50
    data.boardPos = [data.marginX,data.marginY,data.marginX + data.boardW,data.marginY+data.boardH]
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def redrawAll(canvas, data):
    drawBoard(data,canvas)
    drawLines(data,canvas)
    
    
    pass

def drawBoard(data,canvas):
    c = canvas
    c.create_rectangle(data.boardPos[0],data.boardPos[1],data.boardPos[2],
    data.boardPos[3],outline = "gray",)
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if (row + col) % 2 == 0:
                color = "light blue"
            elif (row + col) % 2 == 1: 
                color = "RoyalBlue4"
            
            c.create_rectangle(data.boardPos[0]+row*data.cellSize,
            data.boardPos[1] +  col*data.cellSize,
            data.boardPos[0] + (row+1)*data.cellSize,
            data.boardPos[1] + (col+1)*data.cellSize,
            outline = "", fill = color)
            print(color)
    
    
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
        
    
        
        
    
    
    


####################################
# use the run function as-is
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
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200,800)