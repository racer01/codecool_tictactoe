# tictactoe
import sys
import os

# import curses
from curses import wrapper

import display


def init_table(size):
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


# NOTE: game logic


def check_win(table, step_poz, player):
    """
    Checks and returns whether a player won
    """
    # horizontally ---
    nr = 0
    for cell in table[step_poz['y']]:
        if cell == player:
            nr += 1
        else:
            nr = 0
    # vertically |
    nc = 0
    for row in table:
        if row[step_poz['x']] == player:
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


def check_game_over(table):
    """ Checks and returns whether there's any empty cell """
    game_over = True
    for row in table:
        for cell in row:
            if cell == 0:
                game_over = False
    return game_over


# def asdasd(t, stepPoz, player):
#     """
#     Writes the player's number into the table if the cell at stepPoz is empty
#     """
#     if t[stepPoz['y']][stepPoz['x']] == 0:
#         t[stepPoz['y']][stepPoz['x']] = player
#     return t


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

size = {'y': 3, 'x': 3}


def main(stdscr):
    # init vars
    start_poz = {'y': 2, 'x': 4}
    current_poz = {'y': 0, 'x': 0}
    table = init_table(size)  # init an empty table[row][column]
    locations = display.generate_cell_locations(size, start_poz)  # calc possible step locations[row][col]['y' or 'x']
    cursor_poz = {'y': locations[current_poz['y']][current_poz['x']]['y'],
                  'x': locations[current_poz['y']][current_poz['x']]['x']}
    player = 1

    display.print_table(stdscr, size, start_poz, table, locations)
    # XXX
    # stdscr.addstr(10, 0, str(table))
    # stdscr.move(cursor_poz['y'], cursor_poz['x'])

    stepped = False
    while True:
        display.print_table(stdscr, size, start_poz, table, locations)
        stdscr.addstr(0, 0, "player " + str(player))
        stdscr.move(cursor_poz['y'], cursor_poz['x'])
        k = stdscr.getkey()
        if k == " ":
            stepped = step(table, current_poz, player)
            if check_win(table, current_poz, player) or check_game_over(table):
                break
            if stepped:
                if player == 1:
                    player = 2
                else:
                    player = 1
        elif k == "KEY_DOWN":
            if current_poz['y'] < size['y'] - 1:
                current_poz['y'] += 1
        elif k == "KEY_UP":
            if current_poz['y'] > 0:
                current_poz['y'] -= 1
        elif k == "KEY_LEFT":
            if current_poz['x'] > 0:
                current_poz['x'] -= 1
        elif k == "KEY_RIGHT":
            if current_poz['x'] < size['x'] - 1:
                current_poz['x'] += 1
        else:
            continue

        cursor_poz = {'y': locations[current_poz['y']][current_poz['x']]['y'],
                      'x': locations[current_poz['y']][current_poz['x']]['x']}

        # XXX
        # stdscr.move(0, 0)
        # stdscr.addstr(str(current_poz))
        # stdscr.move(0, 20)
        # stdscr.addstr(str(cursor_poz))
        # stdscr.addstr(15, 0, str(table))
        # --XXX
        stdscr.refresh()
    

def intro():
    # 80x24                                                                                |
    print("                WELCOME TO TICTACTOE!                                           ")
    print("                                          by László Székely-Tóth                ")
    input_string = str(input("Enter the table size as ROWxCOLUMN (default: 3x3): "))
    if input_string:
        col_size, row_size = int(input_string.split('x', 1)[0]), int(input_string.split('x', 1)[1])
        size['y'] = row_size
        size['x'] = col_size

intro()
wrapper(main)
