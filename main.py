def deposit():
    while True:
        amount = input("What would you like to deposit : ")
        if amount.isdigit():
            amount = int(amount)

            if amount >= 1:
                print("grater than zero")
                break
            else:
                print("amount must be grater than zero")
        else:
            print("please enter a number")


deposit()
