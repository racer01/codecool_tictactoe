# tictactoe
import sys
import os

import curses
from curses import wrapper


# NOTE: diplay

def PrintTable(stdscr, size, startPoz, t, locs):
    """
    Prints table borders and content

    Arguments:
    stdscr: standard screen where the table is printed
    size['y' or 'x']: size of the table
    startPoz['y' or 'x']: table padding
    t[row][col]: table
    locs[row][col]['y' or 'x']: table content locations on screen
    """
    # prints borders
    for rowStart in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        stdscr.hline(rowStart, startPoz['x'], curses.ACS_HLINE, (size['x'] * 4) - 1)  # horizontal lines
    for colStart in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
        stdscr.vline(startPoz['y'], colStart, curses.ACS_VLINE, (size['y'] * 2) - 1)  # vertical lines
    for crossY in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        for crossX in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
            stdscr.addch(crossY, crossX, curses.ACS_PLUS)  # line crossings
    # prints table content
    for i in range(size['y']):
        for j in range(size['x']):  # generate all rows
            if t[i][j] == 1:  # player 1
                stdscr.addstr(locs[i][j]['y'], locs[i][j]['x'], "X")
            elif t[i][j] == 2:  # player 2
                stdscr.addstr(locs[i][j]['y'], locs[i][j]['x'], "O")


def InitTable(size):
    """
    Returns a (2d) list[[]] with 0 values as table[row][column]
    """
    t = []
    for i in range(size['y']):
        temp = []
        for j in range(size['x']):
            temp.append(0)  # populating with 0s
        t.append(temp)
    return t


def CalcStepLocations(size, startPoz):
    """
    Returns a list of the on-screen cell locations

    Arguments:
    size: size of table
    startPoz: table padding
    """
    locs = []
    for y in range(size['y']):
        row = []
        for x in range(size['x']):
            row.append({'y': (y * 2) + startPoz['y'], 'x': ((x * 4) + 1) + startPoz['x']})
        locs.append(row)
    return locs


# NOTE: game logic

def CheckWin(table, stepPoz, player):
    """
    Checks and returns whether a player won
    """
    # horizontally ---
    nr = 0
    for cell in table[stepPoz['y']]:
        if cell == player:
            nr += 1
        else:
            nr = 0
    # vertically |
    nc = 0
    for row in table:
        if row[stepPoz['x']] == player:
            nc += 1
        else:
            nc = 0
    # diagonally
    s = min(size['y'], size['x'])  # biggest inner square edge length
    ndl = 0  # diagonal left  /
    ndr = 0  # diagonal right \
    for i in range(s):
        if table[i][s - i - 1] == player:
            ndl += 1
        else:
            ndl = 0
        if table[i][i] == player:
            ndr += 1
        else:
            ndr = 0
    return (nr == s) or (nc == s) or (ndl == s) or (ndr == s)


def CheckGameOver(table):
    """ Checks and returns whether there's any empty cell """
    gameover = True
    for row in table:
        for cell in row:
            if cell == 0:
                gameover = False
    return gameover


# def asdasd(t, stepPoz, player):
#     """
#     Writes the player's number into the table if the cell at stepPoz is empty
#     """
#     if t[stepPoz['y']][stepPoz['x']] == 0:
#         t[stepPoz['y']][stepPoz['x']] = player
#     return t


def CheckStep(table, stepPoz):
    """
    Checks whether stepPoz is an empty cell (no player have stepped there before)
    """
    if table[stepPoz['y']][stepPoz['x']] == 0:
        return True
    else:
        return False


def Step(table, stepPoz, player):
    """
    Steps if it's possible, and returns it's possibility
    """
    valid_step = CheckStep(table, stepPoz)
    if valid_step:
        table[stepPoz['y']][stepPoz['x']] = player
    return valid_step

size = {'y': 3, 'x': 3}


def main(stdscr):
    # init vars
    startPoz = {'y': 2, 'x': 4}
    currentPoz = {'y': 0, 'x': 0}
    table = InitTable(size)  # init an empty table[row][column]
    locations = CalcStepLocations(size, startPoz)  # calc possible step locations[row][col]['y' or 'x']
    cursorPoz = {'y': locations[currentPoz['y']][currentPoz['x']]['y'],
                 'x': locations[currentPoz['y']][currentPoz['x']]['x']}
    player = 1

    PrintTable(stdscr, size, startPoz, table, locations)
    # XXX
    # stdscr.addstr(10, 0, str(table))
    # stdscr.move(cursorPoz['y'], cursorPoz['x'])

    stepped = False
    while True:
        PrintTable(stdscr, size, startPoz, table, locations)
        stdscr.addstr(0, 0, "player " + str(player))
        stdscr.move(cursorPoz['y'], cursorPoz['x'])
        k = stdscr.getkey()
        if k == " ":
            stepped = Step(table, currentPoz, player)
            if CheckWin(table, currentPoz, player) or CheckGameOver(table):
                sys.exit()
            if stepped:
                if player == 1:
                    player = 2
                else:
                    player = 1
        elif k == "KEY_DOWN":
            if currentPoz['y'] < size['y'] - 1:
                currentPoz['y'] += 1
        elif k == "KEY_UP":
            if currentPoz['y'] > 0:
                currentPoz['y'] -= 1
        elif k == "KEY_LEFT":
            if currentPoz['x'] > 0:
                currentPoz['x'] -= 1
        elif k == "KEY_RIGHT":
            if currentPoz['x'] < size['x'] - 1:
                currentPoz['x'] += 1
        else:
            continue

        cursorPoz = {'y': locations[currentPoz['y']][currentPoz['x']]['y'],
                     'x': locations[currentPoz['y']][currentPoz['x']]['x']}

        # XXX
        # stdscr.move(0, 0)
        # stdscr.addstr(str(currentPoz))
        # stdscr.move(0, 20)
        # stdscr.addstr(str(cursorPoz))
        # stdscr.addstr(15, 0, str(table))
        # --XXX
        stdscr.refresh()


def intro():
    input_string = str(input("Enter the table size as ROWxCOLUMN (i.e. 3x3): "))
    col_size, row_size = int(input_string.split('x', 1)[0]), int(input_string.split('x', 1)[1])
    size['y'] = row_size
    size['x'] = col_size

intro()
wrapper(main)
