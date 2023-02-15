import random

ROWS = 3
COLS = 3

symbol_count = {
    "A": 10,
    "B": 4,
    "C": 2,
    "D": 2,
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winning(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    print(columns)
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for key, value in symbols.items():
        for i in range(value):
            all_symbols.append(key)

    columns = []
    symbol = all_symbols[:]
    for col in range(cols):
        column = []

        for row in range(rows):
            value = random.choice(symbol)
            column.append(value)
            symbol.remove(value)

        columns.append(column)

    return columns


def print_slots(columns):
    for row in range(len(columns)):
        for i, column in enumerate(columns):
            if i == len(columns) - 1:
                print(column[row])
            else:
                print(column[row], end=" | ")
        # print()


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


def spin(balance):
    lines = bet_lines()
    while True:

        bet = bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print("you havent enogh money")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines.Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot = print_slots(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print("winnings ", winnings)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")

        spin_ = input("press enter to spin ( q to quit )")
        if spin_ == "q":
            break
        balance += spin(balance)


main()
