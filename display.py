import curses
from curses import wrapper

from point import Point


class Display:
    def __init__(self, stdscr, size, padding):
        """
        Args:
            stdscr: standard screen where the table is printed
            size['y' or 'x']: size of the table
        """
        self.stdscr = stdscr
        self.width = size['width']
        self.height = size['height']
        self.padding = Point(padding['x'], padding['y'])
        self.cell_locations = self.generate_cell_locations()

    def print_table(self, table):
        """
        Prints table borders and content

        Args:
            self: self
            table[row][col]: table
            locs[row][col]['y' or 'x']: table content locations on screen
        """
        # prints borders
        for rowStart in range(self.padding.y + 1, (self.height * 2) + self.padding.y - 1, 2):
            self.stdscr.hline(rowStart, self.padding.x, curses.ACS_HLINE, (self.width * 4) - 1)  # horizontal lines
        for colStart in range(self.padding.x + 3, (self.width * 4) + self.padding.x - 1, 4):
            self.stdscr.vline(self.padding.y, colStart, curses.ACS_VLINE, (self.height * 2) - 1)  # vertical lines
        for crossY in range(self.padding.y + 1, (self.height * 2) + self.padding.y - 1, 2):
            for crossX in range(self.padding.x + 3, (self.width * 4) + self.padding.x - 1, 4):
                self.stdscr.addch(crossY, crossX, curses.ACS_PLUS)  # line crossings
        # prints table content
        for i in range(self.height):
            for j in range(self.width):  # generate all rows
                if table[i][j] == 1:  # player 1
                    self.stdscr.addstr(self.cell_locations[i][j]['y'], self.cell_locations[i][j]['x'], "X")
                elif table[i][j] == 2:  # player 2
                    self.stdscr.addstr(self.cell_locations[i][j]['y'], self.cell_locations[i][j]['x'], "O")

    def generate_cell_locations(self):
        """
        Returns a list of the on-screen cell locations

        """
        locs = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append({'y': (y * 2) + self.padding.y, 'x': ((x * 4) + 1) + self.padding.x})
            locs.append(row)
        return locs

    def move_cursor(self, poz):
        cursor_poz = self.cell_locations[poz['y']][poz['x']]
        self.stdscr.move(cursor_poz['y'], cursor_poz['x'])
