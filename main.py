# tictactoe
import curses
from curses import wrapper

x = 3


def PrintTable(t):
    print(("-" * x * 2) + "-")
    for i in range(x):
        s = "|"
        for j in range(x):
            if t[i][j] == 0:
                s += (" " + "|")
            elif t[i][j] == 1:
                s += ("X" + "|")
            elif t[i][j] == 2:
                s += ("O" + "|")
        print(s)
        print(("-" * x * 2) + "-")


def InitTable():
    t = []
    for i in range(x):
        temp = []
        for j in range(x):
            temp.append(0)
        t.append(temp)
    return t


def CheckWin(table, poz, player):
    # horizontally
    nr = 0
    for cell in table[poz[0]]:
        if cell == player:
            nr += 1
        else:
            nr = 0
    # vertically
    nc = 0
    for row in table:
        if row[poz[1]] == player:
            nc += 1
        else:
            nc = 0
    # diagonally
    nd = 0
    for i in range(x):
        if table[i][i] == player:
            nd += 1
        else:
            nd = 0
    return (nr == 3) or (nc == 3) or (nd == 3)


def StepCol(input_int):
    if (input_int == 1) or (input_int == 4) or (input_int == 7):
        return 0
    elif (input_int == 2) or (input_int == 5) or (input_int == 8):
        return 1
    elif (input_int == 3) or (input_int == 6) or (input_int == 9):
        return 2


def StepRow(input_int):
    if (input_int == 1) or (input_int == 2) or (input_int == 3):
        return 2
    elif (input_int == 4) or (input_int == 5) or (input_int == 6):
        return 1
    elif (input_int == 7) or (input_int == 8) or (input_int == 9):
        return 0


def FormatInput(input_str):
    return [StepRow(int(input_str)), StepCol(int(input_str))]


def Step(t, form_inp, player):
    t[form_inp[0]][form_inp[1]] = player
    return t


def main():
    run = True
    table = InitTable()  # table[row][column]
    PrintTable(table)
    player_won = ""
    while run:
        inp = input("player1: ")
        table = Step(table, FormatInput(inp), 1)
        PrintTable(table)
        if CheckWin(table, FormatInput(inp), 1):
            player_won = "1"
            run = False
            break
        inp = input("player2: ")
        table = Step(table, FormatInput(inp), 2)
        PrintTable(table)
        if CheckWin(table, FormatInput(inp), 2):
            player_won = "2"
            run = False
            break
    print("game over!", "player", player_won, "won!")

main()
