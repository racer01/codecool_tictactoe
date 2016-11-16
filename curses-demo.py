#!/bin/python3.5
from curses import wrapper

import curses


def main(stdscr):

    size = {'y': 10, 'x': 10}
    startPoz = {'y': 2, 'x': 4}

    for rowStart in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        stdscr.hline(rowStart, startPoz['x'], curses.ACS_HLINE, (size['x'] * 4) - 1)
    for colStart in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
        stdscr.vline(startPoz['y'], colStart, curses.ACS_VLINE, (size['y'] * 2) - 1)
    for crossY in range(startPoz['y'] + 1, (size['y'] * 2) + startPoz['y'] - 1, 2):
        for crossX in range(startPoz['x'] + 3, (size['x'] * 4) + startPoz['x'] - 1, 4):
            stdscr.addch(crossY, crossX, curses.ACS_PLUS)

    # (y, x)
    locations = []
    for y in range(size['y']):
        row = []
        for x in range(size['x']):
            row.append({'y': (y * 2) + startPoz['y'], 'x': ((x * 4) + 1) + startPoz['x']})
        locations.append(row)

    stdscr.move(locations[0][1]['y'], locations[0][1]['x'])
    while True:
        a = stdscr.getkey()
        stdscr.clear()

        stdscr.addstr(a)
        stdscr.refresh()
    # stdscr.getkey()

wrapper(main)
