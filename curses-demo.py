#!/bin/python3.5
from curses import wrapper

import curses


def calc_step_locations(size, startPoz):
    locs = []
    for y in range(size['y']):
        row = []
        for x in range(size['x']):
            row.append({'y': (y * 2) + startPoz['y'], 'x': ((x * 4) + 1) + startPoz['x']})
        locs.append(row)
    return locs


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


def main(stdscr):
    size = {'y': 2, 'x': 5}
    startPoz = {'y': 2, 'x': 4}
    currentPoz = {'y': 0, 'x': 0}
    table = InitTable(size)  # table[row][column]
    locations = calc_step_locations(size, startPoz)  # locations[y][x]['y' or 'x']
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

        stdscr.move(0, 0)
        stdscr.addstr(str(currentPoz))

        cursorPoz = {'y': locations[currentPoz['y']][currentPoz['x']]['y'],
                     'x': locations[currentPoz['y']][currentPoz['x']]['x']}
        stdscr.move(0, 20)
        stdscr.addstr(str(cursorPoz))

        stdscr.move(cursorPoz['y'], cursorPoz['x'])

        stdscr.refresh()

wrapper(main)
