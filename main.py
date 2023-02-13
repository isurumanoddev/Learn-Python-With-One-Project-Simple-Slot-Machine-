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
    return amount


def bet_lines():
    while True:
        lines = input("how many lines would you like to bet : ")
        if lines.isdigit():
            lines = int(lines)

            if 3 >= lines >= 1:
                break
            else:
                print("bet lines must be 1 - 3 ")
        else:
            print("please enter a number 1 - 3")
    return lines


def bet_amount():
    while True:
        bet = input("What would you like to bet : ")
        if bet.isdigit():
            bet = int(bet)

            if 1 <= bet <= 100:
                print("grater than zero")
                break
            else:
                print("amount must be grater than zero")
        else:
            print("please enter a number")


def main():
    balance = deposit()
    lines = bet_lines()
    print(balance)
    print(lines)


main()
