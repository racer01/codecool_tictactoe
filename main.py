# tictactoe


def PrintTable(t):
    print("---------")
    for i in range(len(t)):
        s = ""
        for j in range(len(t[0])):
            if t[i][j] == 0:
                s += ("|" + "_" + "|")
            elif t[i][j] == 1:
                s += ("|" + "X" + "|")
            elif t[i][j] == 2:
                s += ("|" + "O" + "|")
        print(s)
        print("---------")


def InitTable():
    t = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(1)
        t.append(temp)
    return t


def main():
    table = InitTable()
    PrintTable(table)
    # input_string = input("írd be a lépést")
    # while
    #     input player1
    #     Step player1
    #     input player2
    #     step player2

main()
