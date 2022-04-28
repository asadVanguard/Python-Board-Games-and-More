"""
File:   battleship.py
Author:  Asad Siddiqui
Date:    4/30/2021
Section: Section 35, Wednesday 11 AM
E-mail:  asiddiq3@umbc.edu
Description: Only going to display board with the ships. Sadly couldn't work on anything else with the project
"""
# importing the board portion of the project
import board

# creating class, BattleshipGame which will operate the functions of the project
class BattleshipGame:
    # size=10 is the size of the board
    def __init__(self, size=10):
        # creating a class variable/object in accordance to the size
        self.size = size

    # first method of the class- running the game
    def run_game(self):
        """
        The goal of this is to order off how to make the boards, and take turns for each player essentially, and
        determine when a player has won or lost in this game
        """

        # setting up player one board via importing the board class from board.py
        player_one_board = board.Board(self.size)
        # setting up player two board via importing hte board class form board.py
        player_two_board = board.Board(self.size)
        # telling player 1 to prepare the fleet
        print("Player 1, prepare to place your fleet.")
        # using our condition checking method to place the ships properly
        self.place_ships(player_one_board)
        # telling player 2 to prepare their fleet
        print("Player 2, prepare to place your fleet.")
        # using our condition checker for our second players board
        self.place_ships(player_two_board)

    # the condition checker method for setting up the board
    def place_ships(self, player_board):
        """
        The goal of this method is to check the conditions of setting up the board
        :param player_board: the new object aka their board that will be set up
        :return: a fully established board
        """
        # calling the method from our second file, board.py to display our board so far for the player
        player_board.display_board(self.size)
        print(player_board.return_position(0, 0))

        # setting up a x and y variable to help establish our needed coords for each ship
        x = 0
        y = 0
        # an empty string that will be replaced with either r or d
        orientation = ""
        # setted up 3 different lists- ships_to_add organizes the ships by name in accordance to our for-loop
        ships_to_add = ["Destroyer", "Submarine", "Cruiser", "Battleship", "Carrier"]
        # 1 minus the true length to help set up the board- this method was more helpful for me
        ship_length = [1, 2, 2, 3, 4]
        # the ship symbols needed
        ship_symbols = ["De", "Su", "Cr", "Ba", "Ca"]
        # until this is proven to be false, we can safely assume that the ships will be overlapping
        overlap_check = True
        # a counter system to help iterate more clearly
        counter = 0
        # for i in range of 5, meaning we will iterate 5 times since there are 5 ships
        for i in range(5):
            # counter will be increased by +1 each time
            counter += 1
            # asking user to input the x y coodinate of the ship
            (x, y) = input("Enter xy coordinates to place the {} ".format(ships_to_add[i])).split()

            # converting both x and y into ints since they were originally strings before
            x = int(x)
            y = int(y)
            # asking user to either orient the pivot right or down
            orientation = input("Enter Right or Down (r or d)")

            # if the orientation is down
            if orientation == "d":
                # we will essentially check each position going downwards along the board's left side
                print(player_board.return_position(x + i, y))
                # we will check as many times as the ship is long
                for i in range(ship_length[i]):
                    # if it is not EMPTY in that position,
                    if player_board.return_position(x + i, y) != " ":
                        # the ships are overlapping therefore, redo the coordinates and orientation
                        overlap_check = True
                    else:
                        # otherwise, they are not overlapping
                        overlap_check = False
            # the concept will be applied here, except for right
            if orientation == "r":
                for i in range(ship_length[i]):
                    # if any where along the lines of checking, it is not EMPTY, that means the ships were overlapping
                    if player_board.return_position(x, y + i) != " ":
                        overlap_check = True
                    # otherwise, once again, they were not actually over lapping
                    else:
                        overlap_check = False

            # if it does so happen to overlap, or it exceeds the size limit by chance, we will keep repeating
            while player_board.return_position(x, y) != " " or (orientation == "d" and self.size - x <= 0) or \
                    (orientation == "r" and self.size - y <= 0) or overlap_check == True:
                # giving user an invalid input message
                print("Invalid position or overlapping ships, try again")
                # telling the user to once again place the ships properly
                (x, y) = input("Enter xy coordinates to place the {}, ".format(ships_to_add[i])).split()
                # converting those coordinates into an x y integer
                x = int(x)
                y = int(y)
                # asking user to input r or d
                orientation = input("Enter Right or Down (r or d) ")
                # if orientation is down
                if orientation == "d":
                    for i in range(ship_length[i]):
                        # we will once again check to see whether they overlap or not
                        if player_board.return_position(x + i, y) != ' ':
                            # and once again, if it is not empty, that means they are over lapping once again, therefore
                            # repeat this while loop
                            overlap_check = True
                        else:
                            # if not, then that means it is officially a legit placement. Carry on.
                            overlap_check = False
                # similar concept will be applied to right too
                if orientation == "r":
                    for i in range(ship_length[i]):
                        # if they are not empty, that means they are overlapping
                        if player_board.return_position(x, y + i) != " ":
                            overlap_check = True
                        # if not, that means it is a legit placement
                        else:
                            overlap_check = False
            # creating a list out of the end coordinates of the ship
            end_position = []
            # printing out the orientation the user wanted
            print(orientation)
            # if it was down
            if orientation == 'd':
                # and our ship length was 2
                if ship_length == 2:
                    # the end pos will only be 1 down, or one away
                    end_position.append(x + 1)
                    # retain the same y
                    end_position.append(y)
                # and our ship length was 3, not 2
                elif ship_length == 3:
                    # the end pos will be 2 down, or 2 away
                    end_position.append(x + 2)
                    # retain the same y
                    end_position.append(y)
                # and our ship length was anything else but those two,
                else:
                    # the end pos will be length-away in accordance to element indexed
                    end_position.append(x + ship_length[i])
                    # still retain the y
                    end_position.append(y)
            # otherwise, if right was chosen
            else:
                # and our ship length was 2
                if ship_length == 2:
                    # retain the x coordinate
                    end_position.append(x)
                    # but rather slide to the right by 1
                    end_position.append(y + 1)
                # and our ship length was 3
                elif ship_length == 3:
                    # retain the same x coordinate
                    end_position.append(x)
                    # slide to the right by 2
                    end_position.append(y + 2)
                # anything else
                else:
                    # we will retain the x coordinate every time
                    end_position.append(x)
                    # but only this time, make it so that we will slide to the right however long the ship reall is
                    end_position.append(y + ship_length[i])

            # the counter helps organize which ship symbol to use
            if counter == 3:
                # 3 means we will use the 3rd element of our list
                player_board.place_ship(ship_symbols[2], [x, y], end_position, orientation)
            elif counter == 4:
                # 4 means we will use the 4th element of our list
                player_board.place_ship(ship_symbols[3], [x, y], end_position, orientation)
            elif counter == 5:
                # 5 means we will use the 5th element of our list
                player_board.place_ship(ship_symbols[4], [x, y], end_position, orientation)
            else:
                # anything else, we will use their ith element of our list.
                player_board.place_ship(ship_symbols[i], [x, y], end_position, orientation)

# main block of code


if __name__ == "__main__":
    # running the battleship game with size 10 as input for the class
    new_game = BattleshipGame(10)
    # running the game officially
    new_game.run_game()





