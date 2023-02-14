import random

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


def get_slot_machine_spin():
    all_symbols = []
    for key, value in symbol_count.items():
        for i in range(value):
            all_symbols.append(key)

    print(all_symbols)
    columns = []

    for col in range(3):
        column = []
        symbol = all_symbols[:]
        for row in range(3):
            value = random.choice(symbol)
            column.append(value)
            symbol.remove(value)
        print(column)
        print(symbol)


get_slot_machine_spin()


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

# main()
