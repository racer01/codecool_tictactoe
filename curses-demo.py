#!/bin/python3.5
from curses import wrapper

import curses


def main(stdscr):
    # Clear screen
    while True:
        a = stdscr.getkey()
        stdscr.clear()
        stdscr.addstr(a)
        stdscr.refresh()
    # stdscr.getkey()

wrapper(main)
