usernameInput = input("Username : ")
passwordInput = input("Password : ")
buyItem = ""
buyQuantity = 0

if usernameInput == "bermby" and passwordInput == "1234":
    print("--- Hello " + usernameInput + " ---")
    print("--- Welcome to Dev Shop ---")
    print("Item List")
    print("1. Apple 5 bath")
    print("2. Mango 10 bath")
    print("3. Cherry 15 bath")

    buyItem = input("Select Item you want to buy : ")
    buyQuantity = int(input("Quantity : "))

    if buyItem == "1":
        print(str(buyQuantity) + " Apple " + str(buyQuantity*5) + " THB")
    elif buyItem == "2":
        print(str(buyQuantity) + " Mango " + str(buyQuantity*10) + " THB")
    elif buyItem == "3":
        print(str(buyQuantity) + " Cherry " + str(buyQuantity*15) + " THB")
    else:
        print("No selected Item")
else:
    print("Username or Password wrong")