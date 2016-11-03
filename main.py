# tictactoe

x = 3  # playing space width & height


def PrintTable(t):
    """ Prints 2d list specified in parameter (t) as the game layout"""
    print(("-" * x * 2) + "-")  # upper edge
    for i in range(x):
        s = "|"  # first left edge
        for j in range(x):  # generate all rows
            if t[i][j] == 0:
                s += (" " + "|")
            elif t[i][j] == 1:
                s += ("X" + "|")
            elif t[i][j] == 2:
                s += ("O" + "|")
        print(s)  # print row
        print(("-" * x * 2) + "-")  # print bottom divider


def InitTable():
    """ Returns a (2d) list[[]] with 0 values """
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


def CheckGameOver(t):
    gameover = False
    for row in t:
        for cell in row:
            if cell == ' ':
                True


def StepCol(input_str):  # Return column from input number
    if (input_str == '1') or (input_str == '4') or (input_str == '7'):
        return 0
    elif (input_str == '2') or (input_str == '5') or (input_str == '8'):
        return 1
    elif (input_str == '3') or (input_str == '6') or (input_str == '9'):
        return 2
    else:
        return -1


def StepRow(input_str):  # Return row from input number
    if (input_str == '1') or (input_str == '2') or (input_str == '3'):
        return 2
    elif (input_str == '4') or (input_str == '5') or (input_str == '6'):
        return 1
    elif (input_str == '7') or (input_str == '8') or (input_str == '9'):
        return 0
    else:
        return -1


def FormatInput(input_str):
    """ Returns formatted input, as [row][col] """
    return [StepRow(input_str), StepCol(input_str)]


def Step(t, form_inp, player):
    if t[form_inp[0]][form_inp[1]] == 0:
        t[form_inp[0]][form_inp[1]] = player
    return t


def CheckStep(t, inp):
    form_inp = FormatInput(inp)
    if -1 in form_inp or t[form_inp[0]][form_inp[1]] != 0:
        return False
    else:
        return True


def main():
    table = InitTable()  # table[row][column]
    PrintTable(table)
    while True:
        # inp = input("player1: ")
        # if -1 not in FormatInput(inp):
        #     table = Step(table, FormatInput(inp), 1)
        # PrintTable(table)
        # if CheckWin(table, FormatInput(inp), 1):
        # if CheckGameOver(table) or player_won != '':
        #     run = False
        #     break

        inp = input("player1: ")
        while not CheckStep(table, inp):
            inp = input("player1: ")
        table = Step(table, FormatInput(inp), 1)
        PrintTable(table)
        if CheckWin(table, FormatInput(inp), 1):
            print("game over! player 1 won!")
            break
        if CheckGameOver(table):
            print("game over!")
            break

        inp = input("player2: ")
        while not CheckStep(table, inp):
            inp = input("player2: ")
        table = Step(table, FormatInput(inp), 2)
        PrintTable(table)
        if CheckWin(table, FormatInput(inp), 2):
            print("game over! player 2 won!")
            break
        if CheckGameOver(table):
            print("game over!")
            break

main()
