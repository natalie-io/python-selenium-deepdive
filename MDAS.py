print()
print("MDAS")
print()
#
items = []

winningNumber = int(input("Enter winning number"))

while True:
    print("Choose option:")
    print("1 - Multiply")
    print("2 - Divide")
    print("3 - Add")
    print("4 - Subtract")
    print("5. Exit")
    print()
    option = int(input("Choose from 1-5: "))
    print()
    print()

    if option == 1:
        num2 = int(input("Enter second number: "))
        winningNumber = winningNumber * num2
        print(winningNumber)
        print()
    elif option == 2:
        num2 = float(input("Enter second number: "))
        winningNumber = winningNumber/num2
        print(winningNumber)
        print()
    elif option == 3:
        num2 = int(input("Enter second number: "))
        winningNumber = winningNumber + num2
        print(winningNumber)
        print()
    elif option == 4:
        num2 = int(input("Enter second number: "))
        winningNumber = winningNumber - num2
        print(winningNumber)
        print()
    elif option == 5:
        break
    else:
        print("Wrong option. Choose only from 1-5")
    print()
