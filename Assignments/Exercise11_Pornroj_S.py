inputNumber = int((input("Input Number : ")))
textStar = ""

for i in range(inputNumber):
    textStar = (" "*(inputNumber-i-1)+("*"*(2*i+1)))
    print(textStar)