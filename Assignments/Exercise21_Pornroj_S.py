from tkinter import *
import math


def leftclickbutton(event):
    labelResult.configure(text=float(textboxWeight.get()) / math.pow(float(textboxHeight.get()) / 100, 2))


mainWindow = Tk()

labelHeight = Label(mainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textboxHeight = Entry(mainWindow)
textboxHeight.grid(row=0, column=1)
labelWeight = Label(mainWindow, text="น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textboxWeight = Entry(mainWindow)
textboxWeight.grid(row=1, column=1)
buttonCalculate = Button(mainWindow, text="คำนวณ BMI")
buttonCalculate.grid(row=2, column=0)
buttonCalculate.bind('<Button-1>', leftclickbutton)
labelResult = Label(mainWindow,text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
#labelResult.configure(text="TEst")

mainWindow.mainloop()