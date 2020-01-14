from tkinter import *

def gameOn():

    openSpaceRef = 0
    clickedCell = 0
    clickedCellValue = 0
    
    def shiftTiles(parentX, parentY, val):

        global openSpace

        if parentY == 0 and parentX == 0:
            clickedCell = 1
        elif parentY == 0 and parentX == 1:
            clickedCell = 2
        elif parentY == 0 and parentX == 2:
            clickedCell = 3
        elif parentY == 1 and parentX == 0:
            clickedCell = 4
        elif parentY == 1 and parentX == 1:
            clickedCell = 5
        elif parentY == 1 and parentX == 2:
            clickedCell = 6
        elif parentY == 2 and parentX == 0:
            clickedCell = 7
        elif parentY == 2 and parentX == 1:
            clickedCell = 8
        elif parentY == 2 and parentX == 2:
            clickedCell = 9

        if val == 0:
            if(clickedCell == 1):
                clickedCellValue = number1Label.cget("text")
            elif(clickedCell == 2):
               clickedCellValue = number2Label.cget("text")
            elif(clickedCell == 3):
                clickedCellValue = number3Label.cget("text")
            elif(clickedCell == 4):
                clickedCellValue = number4Label.cget("text")
            elif(clickedCell == 5):
                clickedCellValue = number5Label.cget("text")
            elif(clickedCell == 6):
                clickedCellValue = number6Label.cget("text")
            elif(clickedCell == 7):
                clickedCellValue = number7Label.cget("text")
            elif(clickedCell == 8):
                clickedCellValue = number8Label.cget("text")
            elif(clickedCell == 9):
                clickedCellValue = number9Label.cget("text")

        else: clickedCellValue = val

        print("clicked: ", clickedCell)
        print("clicked cell text: ", clickedCellValue)
        print("open space: ", openSpace)
        
        movableCells = []
        cellToMove = 0

        # add cells to the right of the open cell
        if openSpace % 3 != 0:
            movableCells.append(openSpace + 1)

        # add cells to the left of the open cell
        if openSpace != 1 and openSpace != 4 and openSpace != 7:
            movableCells.append(openSpace - 1)

        # add cells above the open cell
        if openSpace > 3:
            movableCells.append(openSpace - 3)

        # add cells below the open cell
        if openSpace < 7:
            movableCells.append(openSpace + 3)

        #print("movable cells: ", movableCells)

        for cell in movableCells:
            if clickedCell == cell:
                print("A movable cell was clicked")
                cellToMove = cell

        print("cell to move: ", cellToMove)

        # get reference to openSpace
        if openSpace == 0:
            openSpaceRef = number5Label
        elif openSpace == 1:
            openSpaceRef = number1Label
        elif openSpace == 2:
            openSpaceRef = number2Label
        elif openSpace == 3:
            openSpaceRef = number3Label
        elif openSpace == 4:
            openSpaceRef = number4Label
        elif openSpace == 5:
            openSpaceRef = number5Label
        elif openSpace == 6:
            openSpaceRef = number6Label
        elif openSpace == 7:
            openSpaceRef = number7Label
        elif openSpace == 8:
            openSpaceRef = number8Label
        elif openSpace == 9:
            openSpaceRef = number9Label
        
        print("openSpace text: ", openSpaceRef.cget("text"))


        if cellToMove == 1:
            number1Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 2:
            number2Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 3:
            number3Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 4:
            number4Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 5:
            number5Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 6:
            number6Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 7:
            number7Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 8:
            number8Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell
        elif cellToMove == 9:
            number9Label.config(text="")
            openSpaceRef.config(text=clickedCellValue)
            openSpace = clickedCell


    def callback(event):
        y = event.widget.grid_info()['row']
        x = event.widget.grid_info()['column']
        # frame has no text value yet. will determine in next step
        shiftTiles(x, y, 0)

    def labelClick(event):
        parentY = event.widget.master.grid_info()['row']
        parentX = event.widget.master.grid_info()['column']
        val = event.widget.cget("text")
        shiftTiles(parentX, parentY, val)

    
    
    root = Tk()
    root.title('Tiles')
    root.geometry('{}x{}'.format(500, 500))
    #root.resizable(width=FALSE, height=FALSE)

    # create main containers
    playField = Frame(root, bg="white", height=400, width=500)
    btmFrame = Frame(root, bg="white", height=100, width=500)
    

    # layout main containers   
    root.grid_rowconfigure(0, weight=4)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    playField.grid_columnconfigure(0, weight=1)
    playField.grid_columnconfigure(2, weight=1)
    
    playField.grid(row=0, sticky="nsew")
    btmFrame.grid(row=1, sticky="nsew")

    
    # create the widgets for the top frame
    instrLabel = Label(playField, text="Click a tile next to the open space.\nContinue until the numbers are arranged in ascending order")
    playFrame = Frame(playField, bg="white", height=400, width=400)
    playFrameLeftCol = Frame(playField, bg="white", width=15, height=400)
    playFrameRightCol = Frame(playField, bg="white", width=15, height=400)

    playFrameLeftCol.grid(row=1, column=0, sticky="ew")
    instrLabel.grid(row=0, column=1)
    playFrame.grid(row=1, column=1)
    playFrameRightCol.grid(row=1, column=2, sticky="ew")

    
    number1Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number2Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number3Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number4Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number5Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number6Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number7Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number8Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")
    number9Frame = Frame(playFrame, bg="white", height=100, width=100, borderwidth=2, relief="groove")

    number1Frame.grid_propagate(0)
    number2Frame.grid_propagate(0)
    number3Frame.grid_propagate(0)
    number4Frame.grid_propagate(0)
    number5Frame.grid_propagate(0)
    number6Frame.grid_propagate(0)
    number7Frame.grid_propagate(0)
    number8Frame.grid_propagate(0)
    number9Frame.grid_propagate(0)
    
    number1Label = Label(number1Frame, text="3", font=("Arial", 50))
    number2Label = Label(number2Frame, text="7", font=("Arial", 50))
    number3Label = Label(number3Frame, text="5", font=("Arial", 50))
    number4Label = Label(number4Frame, text="1", font=("Arial", 50))
    number5Label = Label(number5Frame, text="", font=("Arial", 50))
    number6Label = Label(number6Frame, text="2", font=("Arial", 50))
    number7Label = Label(number7Frame, text="8", font=("Arial", 50))
    number8Label = Label(number8Frame, text="4", font=("Arial", 50))
    number9Label = Label(number9Frame, text="6", font=("Arial", 50))

    # layout the widgets in the top frame

    number1Frame.grid(row=0, column=0)
    number2Frame.grid(row=0, column=1)
    number3Frame.grid(row=0, column=2)
    number4Frame.grid(row=1, column=0)
    number5Frame.grid(row=1, column=1)
    number6Frame.grid(row=1, column=2)
    number7Frame.grid(row=2, column=0)
    number8Frame.grid(row=2, column=1)
    number9Frame.grid(row=2, column=2)
    
    number1Label.grid(row=0, column=0)
    number2Label.grid(row=0, column=0)
    number3Label.grid(row=0, column=0)
    number4Label.grid(row=0, column=0)
    number5Label.grid(row=0, column=0)
    number6Label.grid(row=0, column=0)
    number7Label.grid(row=0, column=0)
    number8Label.grid(row=0, column=0)
    number9Label.grid(row=0, column=0)

    number1Label.place(relx=.5, rely=.5, anchor="center")
    number2Label.place(relx=.5, rely=.5, anchor="center")
    number3Label.place(relx=.5, rely=.5, anchor="center")
    number4Label.place(relx=.5, rely=.5, anchor="center")
    number5Label.place(relx=.5, rely=.5, anchor="center")
    number6Label.place(relx=.5, rely=.5, anchor="center")
    number7Label.place(relx=.5, rely=.5, anchor="center")
    number8Label.place(relx=.5, rely=.5, anchor="center")
    number9Label.place(relx=.5, rely=.5, anchor="center")

    number1Frame.bind("<Button-1>", callback)
    number2Frame.bind("<Button-1>", callback)
    number3Frame.bind("<Button-1>", callback)
    number4Frame.bind("<Button-1>", callback)
    number5Frame.bind("<Button-1>", callback)
    number6Frame.bind("<Button-1>", callback)
    number7Frame.bind("<Button-1>", callback)
    number8Frame.bind("<Button-1>", callback)
    number9Frame.bind("<Button-1>", callback)

    number1Label.bind("<Button-1>", labelClick)
    number2Label.bind("<Button-1>", labelClick)
    number3Label.bind("<Button-1>", labelClick)
    number4Label.bind("<Button-1>", labelClick)
    number5Label.bind("<Button-1>", labelClick)
    number6Label.bind("<Button-1>", labelClick)
    number7Label.bind("<Button-1>", labelClick)
    number8Label.bind("<Button-1>", labelClick)
    number9Label.bind("<Button-1>", labelClick)

    def go():
        print("test")
    return root


def checkResponse():
    response = input()
    if response == "y" or response == "Y":
        return "Y"


root = 0


openSpace = 5

print("Hello, world!")
print("This is kind of boring, yeah? Want to play a game instead? (Y/N)")
if checkResponse() == "Y":
    root = gameOn()
root.mainloop()
