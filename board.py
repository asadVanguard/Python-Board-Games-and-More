"""
File:   board.py
Author:  Asad Siddiqui
Date:    4/30/2021
Section: Section 35, Wednesday 11 AM
E-mail:  asiddiq3@umbc.edu
Description: Only going to display board with the ships. Sadly couldn't work on anything else with the project
"""
# creating the class Board

class Board:
    # the goal of this class is to simply get the board done for the game and register shots
    def __init__(self, size):
        # the size of the board will be 10 by default
        self.size = size
        # the board starts off as a simple list
        self.board = []
        # and we will essentially make a 10 by 10 board via for loop system
        for i in range(size):
            # between each 10 iterations, we will create an empty sublist
            self.board.append([])
            # and each sublist will be iterated through 10 times
            for j in range(size):
                # each time, we will append " " for further altercations
                self.board[i].append(" ")
        # just so that the board is neater, this is needed for minor adjustments
        self.board[0][0] = " "

    # FIRST method of the class- the major part which is setting up the board
    def place_ship(self, ship, start_pos, end_pos, direction):
        """
        The goal of this is to do the bulwark of setting up the visuals for the board
        :param ship: the ship symbol
        :param start_pos: starting coordinates the user input
        :param end_pos: the calculated ending coordinates in accordance to orientation and length
        :param direction: the orientation of the pivot point
        :return: a fully set up board
        """
        # always display the board before hand, like a before and after image
        self.display_board(self.size)
        # at the position aka the coordinates the user input, we will put the ship symbol there
        self.board[start_pos[0]][start_pos[1]] = ship
        # the end position will also be the ship
        self.board[end_pos[0]][end_pos[1]] = ship
        # if down was the direction
        if direction == "d":
            # we will iterate as many times as there is a gap in between these two numbers
            for i in range(start_pos[0], end_pos[0]):
                # and keep adding the ship symbol in between
                self.board[start_pos[0] + 1][start_pos[1]] = ship
        # if right was chosen
        else:
            # we will iterate as many times as there are spaces in between these two numbers, y-wise
            for i in range(start_pos[1], end_pos[1]):
                # keep adding the ship symbol in between the two numbers
                self.board[start_pos[0]][end_pos[1] - 1] = ship
        # display the new board now!
        self.display_board(self.size)

    # second method for the x and y coordinates
    def return_position(self, x, y):
        """
        The goal of this is to return the position of the x and y coordinates between each placement
        :param x: the x the user input beforehand
        :param y: the y the user input beforehand
        """
        # always return the position we were at previously to keep track of ship movements and whatnot
        return self.board[x][y]

    # third method for class
    def display_board(self, size):
        """
        Displaying the board for the user through this!
        :param size: The size is needed so we can pricesly layout the design of the board
        :return: the new board design
        """

        # print algorithim for how to set up the board, aesthetically wise!
        print('   ', end='')
        for i in range(size):
            print(i, ' ', end='')
        print('\n')
        for i in range(size):
            print(i, ' ', end='')
            for j in range(size):
                print(self.board[i][j], '|', end='')
            print('\n')








