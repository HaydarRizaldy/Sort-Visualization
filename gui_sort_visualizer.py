from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title('Quick Sort & Bubble Sort Visualization')
root.maxsize(1600, 1080)
root.config(bg='grey')

# Variables
data1 = []
data2 = []
runTime = time.time()

# Functions
def partition(data, head, tail, drawArray, timeTick, canvas):
    border = head
    pivot = data[tail]

    drawArray(data, getColorArray(len(data), head, tail, border, border), canvas)
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawArray(data, getColorArray(len(data), head, tail, border, j, True), canvas)
            time.sleep(timeTick)
            update_runTime(timer1,runTime)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawArray(data, getColorArray(len(data), head, tail, border, j), canvas)
        time.sleep(timeTick)
        update_runTime(timer1,runTime)
        
    # Swap pivot with border value
    drawArray(data, getColorArray(len(data), head, tail, border, tail, True), canvas)
    time.sleep(timeTick)
    update_runTime(timer1,runTime)
    
    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawArray, timeTick, canvas):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawArray, timeTick, canvas)

        # Left partition
        quick_sort(data, head, partitionIdx-1, drawArray, timeTick, canvas)

        # Right partition
        quick_sort(data, partitionIdx+1, tail, drawArray, timeTick, canvas)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('grey')
        else:
            colorArray.append('red')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'white'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

def bubble_sort(data, drawArray, timeTick, canvas):
    global runTime
    runTime = time.time()
    
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawArray(data, ['yellow' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                time.sleep(timeTick)
                update_runTime(timer2,runTime)
                
def update_runTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - runTime)

def drawArray(data, colorArray, canvas):
    canvas.delete("all")
    c_height = 458
    c_width = 560
    x_width = c_width / (len(data) + 1)
    offset = 3
    spacing = x_width / 2
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    
    root.update_idletasks()

def generateArray():
    global data1
    global data2
    data1 = []
    data2 = []

    size = int(sizeEntry.get())
    data1 = random.sample(range(1, size+1), size)

    data2[:] = data1[:]
    drawArray(data1,['red' for x in range(len(data1))], canvas1)
    drawArray(data2,['red' for x in range(len(data2))], canvas2)

def startAlgorithm():
    global data1
    global data2

    global runTime
    runTime = time.time()

    # Run Quick Sort
    quick_sort(data1, 0, len(data1)-1, drawArray, speedScale.get(), canvas1)
    drawArray(data1, ['green' for x in range(len(data1))], canvas1)

    # Run Bubble Sort
    bubble_sort(data2, drawArray, speedScale.get(), canvas2)
    drawArray(data2, ['green' for x in range(len(data2))], canvas2)

# Canvas & Frame
labelFrame1 = Frame(root, width = 300, height = 20, bg='grey')
labelFrame1.grid(row= 0,column=1, padx=20,pady=20)
Label(labelFrame1, text="QUICK SORT", fg='white', bg='grey', font=('Verdana', 12, 'bold')).grid(row=0, column=1)

labelFrame2 = Frame(root, width = 300, height = 20, bg='grey')
labelFrame2.grid(row= 0,column=2, padx=20,pady=20)
Label(labelFrame2, text="BUBBLE SORT", fg='white', bg='grey', font=('Verdana', 12, 'bold')).grid(row=0, column=2)

canvas1 = Canvas(root, width=560, height=460, bg = 'white')
canvas1.grid(row=1, column=1, padx=10, pady=10)

canvas2 = Canvas(root, width=560, height=460, bg = 'white')
canvas2.grid(row=1, column=2, padx=10, pady=10)

buttonFrame = Frame(root, width = 300, height = 100, bg ='grey')
buttonFrame.grid(row = 1, column=0, padx =10, pady=10)

labelFrame3 = Frame(root, width = 500, height = 30, bg='grey')
labelFrame3.grid(row= 2, column=1, padx=20,pady=20)
Label(labelFrame3, text="Running Time (seconds):", fg='white', bg='grey', font=('Courier New', 10, 'bold')).grid(row=1,column=1)
timer1 = Label(labelFrame3, text="", fg='green', bg="white")
timer1.grid(row=2, column=1, pady=20)

labelFrame4 = Frame(root, width = 500, height = 30, bg='grey')
labelFrame4.grid(row= 2, column=2, padx=20,pady=20)
Label(labelFrame4, text="Running Time (seconds):", fg='white', bg='grey', font=('Courier New', 10, 'bold')).grid(row=1,column=2)
timer2 = Label(labelFrame4, text="", fg='green', bg="white")
timer2.grid(row=2, column=2, pady=20)

# Buttons
Label(buttonFrame, text="Insert number of array (integer):", fg='white', bg='grey', font=('Verdana', 10, 'bold')).grid(row=0, column=0, padx=5,pady=5)

sizeEntry = Entry(buttonFrame)
sizeEntry.grid(row=1, column=0, padx=5,pady=5)

generateButton = Button(buttonFrame, text="Generate", fg='white', bg='blue', font=('Verdana', 10, 'bold'), command=generateArray)
generateButton.grid(row=2, column=0, padx=5, pady=5)

speedScale = Scale(buttonFrame, from_=0.001, to=0.500, length=300, digits=3, resolution=0.001, orient=HORIZONTAL, label="Select Speed [seconds]")
speedScale.grid(row=3, column=0, padx=5, pady=5)

startButton = Button(buttonFrame, text="START", fg='white', bg='red', font=('Verdana', 10, 'bold'), command=startAlgorithm)
startButton.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
