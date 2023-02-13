import random

ROWS=3
COLS= 3

def deposit():
    while True:
        amount = input("What would you like to deposit : ")
        if amount.isdigit():
            amount = int(amount)

            if amount >= 1:

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

                break
            else:
                print("amount must be grater than zero")
        else:
            print("please enter a number")
    return bet


def main():
    balance = deposit()
    lines = bet_lines()
    while True:

        bet = bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print("you havent enogh money")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines.Total bet is ${total_bet}")


main()
