# tictactoe
import sys
import os

import curses
from curses import wrapper

from display import Display
from point import Point


def init_table(size):
    """
    Returns a list of lists with 0 values, as table[row][column]

    Args:
        size: a dictionary with the size of the list of lists,
            in {'width': x, 'height': y} format

    Returns:
        list of lists full of 0s
    """
    t = []
    for i in range(size['height']):
        temp = []
        for j in range(size['width']):
            temp.append(0)  # populating with 0s
        t.append(temp)
    return t


# NOTE: game logic


def check_win(table, step_poz, player):
    """
    Checks and returns whether a player won
    """
    s = 3  # min(size['y'], size['x'])  # biggest inner square edge length
    # horizontally ---
    nr = 0
    for cell in table[step_poz['y']]:
        if cell == player:
            nr += 1
            if nr == s:
                return True
        else:
            nr = 0
    # vertically |
    nc = 0
    for row in table:
        if row[step_poz['x']] == player:
            nc += 1
            if nc == s:
                return True
        else:
            nc = 0
    # diagonally
    ndl = 0  # diagonal left  /
    ndr = 0  # diagonal right \
    for i in range(s):
        if table[i][s - i - 1] == player:
            ndl += 1
            if ndl == s:
                return True
        else:
            ndl = 0
        if table[i][i] == player:
            ndr += 1
            if ndr == s:
                return True
        else:
            ndr = 0
    return False


def check_game_over(table):
    """ Checks and returns whether there's any empty cell """
    game_over = True
    for row in table:
        for cell in row:
            if cell == 0:
                game_over = False
    return game_over


def check_step(table, step_poz):
    """
    Checks whether step_poz is an empty cell (no player have stepped there before)
    """
    if table[step_poz['y']][step_poz['x']] == 0:
        return True
    else:
        return False


def step(table, step_poz, player):
    """
    Steps if it's possible, and returns it's possibility
    """
    valid_step = check_step(table, step_poz)
    if valid_step:
        table[step_poz['y']][step_poz['x']] = player
    return valid_step


def color_win(stdscr, size, start_poz, table, locs):
    """ NOT IMPLEMENTED """
    # prints table content
    for i in range(size['y']):
        for j in range(size['x']):  # generate all rows
            if table[i][j] == 1:  # player 1
                stdscr.addstr(locs[i][j]['y'], locs[i][j]['x'], "X")
            elif table[i][j] == 2:  # player 2
                stdscr.addstr(locs[i][j]['y'], locs[i][j]['x'], "O")


def main(stdscr):
    # init vars
    run = 1
    current_poz = {'y': 0, 'x': 0}
    size = {'height': input_size['height'] or 3,
            'width': input_size['width'] or 3}
    table = init_table(size)  # init an empty table[row][column]
    # init display
    padding = {'y': 2, 'x': 4}
    display = Display(stdscr, size, padding)

    player = 1

    display.print_table(table)

    stepped = False
    while run == 1:
        stdscr.addstr(0, 0, "player " + str(player))
        display.move_cursor(current_poz)
        k = stdscr.getkey()
        if k == " ":
            stepped = step(table, current_poz, player)
            if check_game_over(table):
                run = 0
            elif check_win(table, current_poz, player):
                run = 2
            elif stepped:
                if player == 1:
                    player = 2
                else:
                    player = 1
        elif k == "KEY_DOWN":
            if current_poz['y'] < size['height'] - 1:
                current_poz['y'] += 1
        elif k == "KEY_UP":
            if current_poz['y'] > 0:
                current_poz['y'] -= 1
        elif k == "KEY_LEFT":
            if current_poz['x'] > 0:
                current_poz['x'] -= 1
        elif k == "KEY_RIGHT":
            if current_poz['x'] < size['width'] - 1:
                current_poz['x'] += 1
        else:
            continue
        display.print_table(table)

        stdscr.refresh()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.curs_set(False)
    if run == 0:
        stdscr.addstr(1, 0, "You lose!", curses.color_pair(1))
    elif run == 2:
        stdscr.addstr(1, 0, "Player " + str(player) + " won!", curses.color_pair(2))
    stdscr.addstr(10, 0, "Press any key to exit!")
    stdscr.refresh()
    stdscr.getkey()


def intro():
    # 80x24                                                                                |
    print("     _____ _    _____        _____                                              ")
    print("    |_   _(_)  |_   _|      |_   _|                                             ")
    print("      | |  _  ___| | __ _  ___| | ___   ___                                     ")
    print("      | | | |/ __| |/ _` |/ __| |/ _ \ / _ \                                    ")
    print("      | | | | (__| | (_| | (__| | (_) |  __/                                    ")
    print("      \_/ |_|\___\_/\__,_|\___\_/\___/ \___|                                    ")
    print("                                                                                ")
    print("________________________________________ _______________________ _______  ")
    print("\__   __\__   __(  ____ \__   __(  ___  (  ____ \__   __(  ___  (  ____ \ ")
    print("   ) (     ) (  | (    \/  ) (  | (   ) | (    \/  ) (  | (   ) | (    \/ ")
    print("   | |     | |  | |        | |  | (___) | |        | |  | |   | | (__     ")
    print("   | |     | |  | |        | |  |  ___  | |        | |  | |   | |  __)    ")
    print("   | |     | |  | |        | |  | (   ) | |        | |  | |   | | (       ")
    print("   | |  ___) (__| (____/\  | |  | )   ( | (____/\  | |  | (___) | (____/\ ")
    print("   )_(  \_______(_______/  )_(  |/     \(_______/  )_(  (_______(_______/ ")
    print("                                                                          ")
    input_string = str(input("Enter the table size as ROWxCOLUMN (default: 3x3, max 7x7): "))
    if input_string:
        col_size, row_size = int(input_string.split('x', 1)[0]), int(input_string.split('x', 1)[1])
        return {'height': row_size, 'width': col_size}
    else:
        return {'height': 3, 'width': 3}


input_size = intro()
wrapper(main)
