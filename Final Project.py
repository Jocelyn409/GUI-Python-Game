from tkinter import *
#import binascii
import string
import random


window = Tk()
window.minsize(width=1000, height=700)
window.resizable(False, False)
window.title("Bit Guesser")

randomCharacter = ''

def randomize(): # add options somewhere to choose what is in the random character list??? new button??
    global randomCharacter
    randomCharacter = random.choice(string.printable)

def convertToBinary(character):
    return bin(int.from_bytes(character.encode(), 'big'))[2:]

def showPath():
    start = "+"
    destination = "@"
    upFull = "*\n*\n*"
    upRight = "\n           ********\n*"
    rightFull = "*****************"
    rightUp = "*\n*********            \n"
    rowPos = 7
    columnPos = 0

    # Create new 8x8 grid every time. This is so we can clear the entire gridFrame when resetting.
    for row in range(8):
        for column in range(8):
            square = Frame(master=gridFrame, width=110, height=70, bg="#222222",
                           highlightbackground="#444444", highlightthickness="1")
            square.grid(row=row, column=column)

    startingPoint = Label(gridFrame, text=start, bg="#222222",
                          fg="white", font=(25)).grid(row=rowPos, column=columnPos)

    randomize()
    binary = convertToBinary(randomCharacter)
    length = len(binary)
    stringCounter = 0
    direction = ""
    print(binary)
    print(randomCharacter)
    for n in binary:
        if length != stringCounter+1:
            if n == "1": # 1 means go right
                columnPos += 1
                if binary[stringCounter+1] == "1": # Next position is to the right
                    direction = rightFull
                elif binary[stringCounter+1] == "0": # Next position is up
                    direction = rightUp
                labelDirection = Label(gridFrame, text=direction, bg="#222222", fg="white",
                                 font=(25)).grid(row=rowPos, column=columnPos)
            elif n == "0": # 0 means go up
                rowPos -= 1
                if binary[stringCounter+1] == "0": # Next position is up
                    direction = upFull
                elif binary[stringCounter+1] == "1": # Next position is to the right
                    direction = upRight
                labelDirection = Label(gridFrame, text=direction, bg="#222222", fg="white",
                                 font=(25)).grid(row=rowPos, column=columnPos)
            stringCounter += 1
    # Last update of positions wasn't calculated in for loop; it is done below
    if binary[stringCounter] == "1":
        columnPos += 1
    elif binary[stringCounter] == "0":
        rowPos -= 1
    final = Label(gridFrame, text=destination, bg="#222222", fg="white",
                  font=(25)).grid(row=rowPos, column=columnPos)


def pressReset():
    randomize()
    input.delete(0, END) # Reset input
    labelAnswer.config(text="")
    showPath()

# Function will
def pressEnter():
    global randomCharacter

    input.delete(1, END) # Deletes all but first character
    if input.get() == "":
        labelAnswer.config(text="¯\_(ツ)_/¯")
    elif input.get() == randomCharacter:
        labelAnswer.config(text="Correct answer")
    else:
        labelAnswer.config(text="Incorrect answer")

# Frames
backgroundFrame = Frame(master=window, height=620, bg="#333333")
backgroundFrame.pack_propagate(False)
backgroundFrame.pack(fill=X)
inputFrame = Frame(master=window, height=80, bg="#444444")
inputFrame.pack_propagate(False)
inputFrame.pack(fill=X)
gridFrame = LabelFrame(master=backgroundFrame, width=750, height=600, bg="#222222")
gridFrame.pack_propagate(0)
gridFrame.pack(padx=20,pady=20)

showPath()

# Items
input = Entry(inputFrame, width=18, borderwidth=2, bg="#333333", fg="white", justify=CENTER)
submitButton = Button(inputFrame, width=15, height=2, text="Enter", command=pressEnter, bg="green")
resetButton = Button(inputFrame, text="Reset", command=pressReset, bg="red", height=80, width=10)
labelAnswer = Label(inputFrame, text="", bg="#444444", fg="#999999")
resetButton.pack(side=LEFT)
submitButton.pack(side=BOTTOM)
input.pack(side=BOTTOM)
labelAnswer.pack(side=BOTTOM)

window.configure()
window.mainloop()