def greet():
    print("---------------------")
    print("|   Здравствуйте!   |")
    print("|   Начинаем игру   |")
    print("| 'Крестики-нолики' |")
    print("---------------------")
    print("     Инструкция:     ")
    print("---------------------")
    print("| Формат ввода: xy  |")
    print("|Координаты вводятся|")
    print("|    БЕЗ ПРОБЕЛА!   |")
    print("| x - номер строки  |")
    print("| y - номер столбца |")
    print("---------------------")


def show():
    print("    y             ")
    print("    | 0 | 1 | 2 | ")
    print("x --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = list(input("         Ваш ход: "))

        if len(cords) != 2:
            print(" Не корректный формат ввода! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("Ячейка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            return "Выиграл КРЕСТИК (Х) !!!"
        if symbols == ["0", "0", "0"]:
            return "Выиграл НОЛИК (0) !!!"
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        show()
        print(check_win())
        break

    if count == 9:
        show()
        print(" Ничья!")
        break

