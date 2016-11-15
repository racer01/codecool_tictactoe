#!/bin/python3.5
from curses import wrapper

import curses


def main(stdscr):
    # Clear screen
    while True:
        a = stdscr.getkey()
        stdscr.clear()

        stdscr.addstr(a)
        stdscr.vline(5, 5, curses.ACS_VLINE, 5)
        stdscr.refresh()
    # stdscr.getkey()

wrapper(main)
