from tkinter import *
import math


def calculate_bmi(height, weight):
    height = float(height)
    weight = float(weight)
    bmi = weight / math.pow(height/100, 2)

    bmi_result = ""
    if bmi >= 30.0:
        bmi_result = "อ้วนมาก"
    elif bmi >= 25.0:
        bmi_result = "อ้วน"
    elif bmi >= 23.0:
        bmi_result = "น้ำหนักเกิน"
    elif bmi >= 18.6:
        bmi_result = "น้ำหนักปกติ"
    elif bmi < 18.6:
        bmi_result = "ผอมเกินไป"

    return bmi_result


def leftclickbutton(event):
    bmi_result = calculate_bmi(textboxHeight.get(), textboxWeight.get())
    labelResult.configure(text=bmi_result)


#####GUI Setup#####

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
labelResult = Label(mainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)

mainWindow.mainloop()
