import curses
from curses import wrapper


def print_table(stdscr, size, start_poz, table, locs):
    """
    Prints table borders and content

    Arguments:
    stdscr: standard screen where the table is printed
    size['y' or 'x']: size of the table
    start_poz['y' or 'x']: table padding
    table[row][col]: table
    locs[row][col]['y' or 'x']: table content locations on screen
    """
    # prints borders
    for rowStart in range(start_poz['y'] + 1, (size['y'] * 2) + start_poz['y'] - 1, 2):
        stdscr.hline(rowStart, start_poz['x'], curses.ACS_HLINE, (size['x'] * 4) - 1)  # horizontal lines
    for colStart in range(start_poz['x'] + 3, (size['x'] * 4) + start_poz['x'] - 1, 4):
        stdscr.vline(start_poz['y'], colStart, curses.ACS_VLINE, (size['y'] * 2) - 1)  # vertical lines
    for crossY in range(start_poz['y'] + 1, (size['y'] * 2) + start_poz['y'] - 1, 2):
        for crossX in range(start_poz['x'] + 3, (size['x'] * 4) + start_poz['x'] - 1, 4):
            stdscr.addch(crossY, crossX, curses.ACS_PLUS)  # line crossings
    # prints table content
    for i in range(size['y']):
        for j in range(size['x']):  # generate all rows
            if table[i][j] == 1:  # player 1
                stdscr.addstr(locs[i][j]['y'], locs[i][j]['x'], "X")
            elif table[i][j] == 2:  # player 2
                stdscr.addstr(locs[i][j]['y'], locs[i][j]['x'], "O")


def generate_cell_locations(size, start_poz):
    """
    Returns a list of the on-screen cell locations

    Arguments:
    size: size of table
    start_poz: table padding
    """
    locs = []
    for y in range(size['y']):
        row = []
        for x in range(size['x']):
            row.append({'y': (y * 2) + start_poz['y'], 'x': ((x * 4) + 1) + start_poz['x']})
        locs.append(row)
    return locs
