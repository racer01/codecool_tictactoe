# tictactoe
import sys
import os

import curses
from curses import wrapper

x = 3  # playing space width & height


# NOTE: diplay

def PrintTable(stdscr, size, startPoz, t, locs):
    for rowStart in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        stdscr.hline(rowStart, startPoz['x'], curses.ACS_HLINE, (size['x'] * 4) - 1)
    for colStart in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
        stdscr.vline(startPoz['y'], colStart, curses.ACS_VLINE, (size['y'] * 2) - 1)
    for crossY in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        for crossX in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
            stdscr.addch(crossY, crossX, curses.ACS_PLUS)

    for i in range(size['y']):
        for j in range(size['x']):  # generate all rows
            if t[i][j] == 1:
                stdscr.addch(locs[i][j]['y'], locs[i][j]['x'], "X")
            elif t[i][j] == 2:
                stdscr.addch(locs[i][j]['y'], locs[i][j]['x'], "O")


def InitTable(size):
    """ Returns a (2d) list[[]] with 0 values """
    # table[row][column]
    t = []
    for i in range(size['y']):
        temp = []
        for j in range(size['x']):
            temp.append(0)
        t.append(temp)
    return t


def calc_step_locations(size, startPoz):
    locs = []
    for y in range(size['y']):
        row = []
        for x in range(size['x']):
            row.append({'y': (y * 2) + startPoz['y'], 'x': ((x * 4) + 1) + startPoz['x']})
        locs.append(row)
    return locs


# NOTE: game logic

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
    ndl = 0  # diagonal left
    ndr = 0  # diagonal right
    for i in range(x):
        if table[i][x - i - 1] == player:
            ndl += 1
        else:
            ndl = 0
        if table[i][i] == player:
            ndr += 1
        else:
            ndr = 0
    return (nr == x) or (nc == x) or (ndl == x) or (ndr == x)


def CheckGameOver(t):
    """ Check if there's any empty cell """
    gameover = True
    for row in t:
        for cell in row:
            if cell == 0:
                gameover = False
    return gameover


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


# FIXME
def FormatInput(input_str):
    """ Returns formatted input, as [row][col] """
    return [StepRow(input_str), StepCol(input_str)]

#FIXME
def Step(t, form_inp, player):
    if t[form_inp[0]][form_inp[1]] == 0:
        t[form_inp[0]][form_inp[1]] = player
    return t


def CheckStep(t, inp):
    """ Check if input is valid
        invalid inputs: out of range, not free cell, or x"""
    form_inp = FormatInput(inp)
    if -1 in form_inp or t[form_inp[0]][form_inp[1]] != 0 or inp == 'x':
        return False
    else:
        return True

# FIXME
def Progress(table, pl):
    inp = input("player" + str(pl) + ": ")
    while not CheckStep(table, inp):
        if inp == "x":
            print("Exiting...")
            sys.exit()
        inp = input("player" + str(pl) + ": ")
    table = Step(table, FormatInput(inp), pl)
    PrintTable(table)
    if CheckWin(table, FormatInput(inp), pl):
        print("game over! player " + str(pl) + " won!")
        return True
    if CheckGameOver(table):
        print("game over!")
        return True


def main(stdscr):
    size = {'y': 2, 'x': 5}
    startPoz = {'y': 2, 'x': 4}
    currentPoz = {'y': 0, 'x': 0}
    table = InitTable(size)  # init an empty table[row][column]
    locations = calc_step_locations(size, startPoz)  # calc possible step locations[row][col]['y' or 'x']
    cursorPoz = {'y': locations[currentPoz['y']][currentPoz['x']]['y'],
                 'x': locations[currentPoz['y']][currentPoz['x']]['x']}

    PrintTable(stdscr, size, startPoz, table, locations)
    stdscr.move(cursorPoz['y'], cursorPoz['x'])
    # XXX
    stdscr.addstr(10, 0, str(table))

    while True:
        k = stdscr.getkey()
        if k == "KEY_DOWN":
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
        elif k == " ":
            pass
        else:
            continue

        PrintTable(stdscr, size, startPoz, table, locations)
        cursorPoz = {'y': locations[currentPoz['y']][currentPoz['x']]['y'],
                     'x': locations[currentPoz['y']][currentPoz['x']]['x']}

        # XXX
        stdscr.move(0, 0)
        stdscr.addstr(str(currentPoz))
        stdscr.move(0, 20)
        stdscr.addstr(str(cursorPoz))
        # XXX

        stdscr.move(cursorPoz['y'], cursorPoz['x'])
        stdscr.refresh()
'''
        if Progress(table, 1):
            break
        if Progress(table, 2):
            break
'''
wrapper(main)
