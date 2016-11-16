#!/bin/python3.5
from curses import wrapper

import curses


def main(stdscr):

    sizeX = 10
    sizeY = 10

    startX = 3
    startY = 3

    for rowStart in range(startY + 1, (sizeY * 2) + startY - 1, 2):
        stdscr.hline(rowStart, startX, curses.ACS_HLINE, (sizeX * 4) - 1)
    for colStart in range(startX + 3, (sizeX * 4) + startX - 1, 4):
        stdscr.vline(startY, colStart, curses.ACS_VLINE, (sizeY * 2) - 1)
    for crossY in range(startY + 1, (sizeY * 2) + startY - 1, 2):
        for crossX in range(startX + 3, (sizeX * 4) + startX - 1, 4):
            pass

    locations = (((0, 1), (0, 5), (0, 9)),
                 ((2, 1), (2, 5), (2, 9)),
                 ((4, 1), (4, 5), (4, 9)))

    stdscr.move(locations[0][1][0], locations[0][1][1])
    while True:
        a = stdscr.getkey()
        stdscr.clear()

        stdscr.addstr(a)
        stdscr.refresh()
    # stdscr.getkey()

wrapper(main)
