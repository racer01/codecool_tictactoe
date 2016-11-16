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


def print_table(stdscr, size, startPoz):
    for rowStart in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        stdscr.hline(rowStart, startPoz['x'], curses.ACS_HLINE, (size['x'] * 4) - 1)
    for colStart in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
        stdscr.vline(startPoz['y'], colStart, curses.ACS_VLINE, (size['y'] * 2) - 1)
    for crossY in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        for crossX in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
            stdscr.addch(crossY, crossX, curses.ACS_PLUS)


def main(stdscr):

    size = {'y': 10, 'x': 10}
    startPoz = {'y': 2, 'x': 4}
    currentPoz = {'y': 0, 'x': 0}

    print_table(stdscr, size, startPoz)
    # (y, x)
    locations = calc_step_locations(size, startPoz)

    stdscr.move(locations[currentPoz['y']][currentPoz['x']]['y'], locations[currentPoz['y']][currentPoz['x']]['x'])
    while True:
        k = stdscr.getkey()
        # stdscr.clear()
        # stdscr.addstr(k)
        if k == "KEY_DOWN":
            if currentPoz['y'] < size['y'] - 1:
                currentPoz['y'] += 1
        elif k == "KEY_UP":
            if currentPoz['y'] > 1 - 1:
                currentPoz['y'] -= 1
        elif k == "KEY_LEFT":
            if currentPoz['x'] > 1 - 1:
                currentPoz['x'] -= 1
        elif k == "KEY_RIGHT":
            if currentPoz['x'] < size['x'] - 1:
                currentPoz['x'] += 1
        else:
            continue
        stdscr.move(0, 0)
        stdscr.addstr(str(currentPoz))
        stdscr.move(locations[currentPoz['y']][currentPoz['x']]['y'], locations[currentPoz['y']][currentPoz['x']]['x'])

        stdscr.refresh()
    # stdscr.getkey()

wrapper(main)
