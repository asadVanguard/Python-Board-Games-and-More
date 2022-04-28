"""
File:    mancala.py
Author:  Asad Siddiqui
Date:    4/5/2021
Section: Wednesday 11 AM sect 35
E-mail:  asiddiq3@umbc.edu
Description: The goal of this project is to play a game called Mancala. Very fun indeed

"""

# defining our main game function
def run_game(conditional_counter_top, conditional_counter_bottom):
    """
    The goal of this function, simply put it, is to make the game work as intended, really. Nothing more to it.
    Some variables were made to make this game function a bit more smoothly!
    :param conditional_counter_top: If this checks out to 6 (see more in the mancala_checker function) game will end
    :param conditional_counter_bottom: If this checks out to 6 too (see more in the mancala_checker function) game ends
    :return: This will return who won the game ultimately
    """
    # creating a counter to help take turns for this game
    turn_counter = 0
    # made a counter that will keep track of which cups will be empty ultimately
    empty_counter = 0

    # so ultimately, we will keep this direct flow of the game as long as the game is running forever!
    while empty_counter < 6:
        # first, we will determine who needs to go first
        take_turns(turn_counter)
        # player can select who will go first, and the list which has the all of the data will always transfer in between sessions
        mancala_callout(cup_selection, data_list)
        # every time, call this function to set up the board
        board_design()

        # once we have 6 empty cups in a row, game is over
        empty_counter = mancala_data_checker()
        # until then, keep adding + 1 between each turn
        turn_counter = turn_counter + 1
    # if Player 1's cup has more stones than Player 2's
    if data_list[1] > data_list[3]:
        # return this
        return print('Game is over! Player {} wins!'.format(player_a))
    # if not, return that the other player has won
    else:
        return print('Game is over! Player {} wins!'.format(player_b))


# a function to get our players
def get_players():
    """
    To get the players, we use this function. Pretty self explanatory
    :return: player_a and player_b's names.
    """
    player_a = input('Please enter name for player A. ')

    player_b = input('Please enter name for player B. ')

    list_of_players.append(player_a)
    list_of_players.append(player_b)
    return list_of_players


def board_design():
    """
    No inputs needed for this (parameters). We will keep this as simple as possible
    :return: The board it self with base contents
    """
    # height of our board being made
    height = 80
    # width of our board being made
    width = 13
    # the exact measurement to make the width and height align- drawing out board via For Loop style!
    for i in range(height - 1):
        # printing * signs with no space in between to form ****** for example
        print('*', end='')
    # the exact width needed for this board design
    for j in range(width):
        # a rough measurement of how to display the board I will need. Lots of tab spaces to space out the *'s
        print('*', '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', "  " '*', end='\n')
        # at certain j-values, or along the width, we need to align our cups according to where they may belong
        if j == 1:
            # a decent measurement of how to align our display board for the cups for the Mancala game
            print('\t', '\t', 'Cup 1: {}'.format(cup_1[1]), '\t', 'Cup 2: {}'.format(cup_2[1]), '\t', 'Cup 3: {}'.format(cup_3[1]),
                  '\t', 'Cup 4: {}'.format(cup_4[1]), '\t', 'Cup 5: {}'.format(cup_5[1]), '\t', 'Cup 6: {}'.format(cup_6[1]))
        # another j-value in which we will finally align the Mancala-cups for the players.
        elif j == 6:
            # using tab spaces where needed, and generic names to make it more simple
            print('\t', 'Player 2 Stones: {}'.format(data_list[3]), '\t\t\t\t\t\t\t\t', 'Player 1 Stones: {}'.format(data_list[1]))
        # the last j-value for aligning the rest of our cups
        elif j == 11:
            # approximate measurement to align the cups
            print('\t', '\t', 'Cup 13: {}'.format(cup_13[1]), '\t', 'Cup 12: {}'.format(cup_12[1]), '\t',
                  'Cup 11: {}'.format(cup_11[1]), '\t', 'Cup 10: {}'.format(cup_10[1]), '\t',
                  'Cup 9: {}'.format(cup_9[1]), '\t', 'Cup 8: {}'.format(cup_8[1]))
    # final For-Loop for designing the outline of our board.
    for k in range(height):
        # printing * in the form of ****** with no spaces in between in a nutshell
        print('*', end='')

# a helper function to keep track of turns
def take_turns(turn_counter):
    """
    A function meant to help keep track of whose turn it is
    turn_counter:  a parameter set up in the main-game function. It will transfer over to this helper function and
            help determine whose turn it is
    :return: returns the cup in which each player selected, one at a time.
    """
    # a basic if statement system that will mod by 2, and every even turn it will be player 1's turn.
    if turn_counter % 2 == 0:
        return print('It is player 1\'s turn.')
    # if not, it's player 2's turn
    else:
        return print('It is player 2\'s turn.')

# this function is a helper function to keep track of the scores and whatnot
def mancala_data_checker():
    """
    No input is needed for this function since this is being kept to a bare minimal for simplicity!
    :return: The results of the game in terms of either True (the game is over) or False (the game continues)
    """
    # a counter to keep track of how many empty slots there are in the top portion, and will reset each time this
    # function is called
    empty_counter_top = 0
    # a not-so-helpful variable to keep track of how many cups still have stones in them
    still_full_counter_top = 0
    # a for loop meant to cycle through each of the top cups and determine which don't have stones in them
    for i in range(len(top_cups)):
        # if the stone count is = 0
        if top_cups[i][1] == 0:
            # add a + 1 to this variable
            empty_counter_top = empty_counter_top + 1
        # if not,
        else:
            # then add a + 1 to the full variable
            still_full_counter_top = still_full_counter_top + 1

    """
    Similar concept is applied for the bottom counters! 
    """
    empty_counter_bottom = 0
    still_full_counter_bottom = 0
    for i in range(len(bottom_cups)):
        if bottom_cups[i][1] == 0:
            empty_counter_bottom = empty_counter_bottom + 1
        else:
            still_full_counter_bottom = still_full_counter_bottom + 1

    """
    Conditionals to determine whether we should return the empty counters for top and bottom or not.
    
    This will also determine if something a tie game ahead of time
    """

    # if ALL cups up top are empty
    if empty_counter_top == 6:
        # and player 1 has more stones than player 2
        if data_list[1] > data_list[3]:
            # give back the value of 6, basically to break the while-loop of the run_game function
            return empty_counter_top
        # if player 2 > player 1
        elif data_list[1] < data_list[3]:
            # return the value of 6 for that same reason
            return empty_counter_top
    # if ALL bottom cups are empty
    elif empty_counter_bottom == 6:
        # and player 1 stones > player 2
        if data_list[1] > data_list[3]:
            # return the value of 6 (basically) to break our while loop as well
            return empty_counter_bottom
        # if player 2 > player 1
        elif data_list[1] < data_list[3]:
            # return a value of 6 basically too for the same reason
            return empty_counter_bottom
    # if not, just return board at least and keep playing the game
    else:
        return empty_counter_top


def mancala_callout(cup_movement, previous_results):
    """
    This is the pseudo-main function. In all honesty, this is extremely long and makes up the bulk of this project.
    I would suggest you read the first couple of commenting to get the jist, as I did repeat the same level of comments
    and simplified them with ' ' ' - style of commenting later on. My apologies if this is very long.
    :param cup_movement: player chooses a cup, and this will 'move' the stones clockwise
    :return: new data for the top and bottom cups, and also the mancala_data_checker function to recheck everything
    """
    # player 1 or 2 chooses a cup to move. YOU MUST FOLLOW THE FORMAT! I think it makes the player think twice as much
    # as they will now have to type in cup_# to confirm what they really want.
    cup_movement = input('Player, select a cup to choose from. (1, etc.) ')
    # if you select cup 1 and cup 1 is not empty
    if cup_movement == '1' and cup_1[1] != 0:

        # iterate as many times as there are stones in cup 1
        for i in range(cup_1[1]):
            # with each cup, add +1 to their stone collection
            top_cups[i+1][1] = top_cups[i + 1][1] + 1
        # set cup 1's stones = 0
        cup_1[1] = 0

        # return the main list of data to keep cycling and updating it per turn
        return data_list

    # if the player chose cup 2 and it's not empty
    elif cup_movement == '2' and cup_2[1] != 0:

        # this is a pseudo-iterator variable, except for the top row of cups
        j = 2
        # this is another pseudo-iterator variable, except for the bottom row of cups
        k = 0
        # this is the last pseudo-iterator variable
        l = 8


        # a list of the remaining cups, including cup 1. The goal is to have j match one of those numbers
        remaining_top = [2, 3, 4, 5, 6]
        # another list with the remaining cups of the bottom list. The goal is to have k match one of those numbers
        remaining_bottom = [8, 9, 10, 11, 12, 13]
        # theoretically speaking, I made this to ensure that through each iteration, we won't accidentally keep putting
        # all of our stones into the top row only, pretty much.

        # iterate as many times as there are stones. So if there are now 5 stones in cup_2, repeat this process 5 times
        for i in range(cup_2[1]):
            # as long as j-variable matches one of those terms in the list for remaining top + 1 (a ratio to make this work)
            if j + 1 in remaining_top:
                # we'll add +1 to the cups that are followed after cup_2 ! So if j = 4, we'll come into here, and add +1
                # to another cup that aligns with it (in this example, cup_5 will be called)
                top_cups[j][1] = top_cups[j][1] + 1
                # add + 1 to our j variable to continue with this process
                j = j + 1
            # if j ever so happens to be = 6, that will align with player 1's stones, therefore...
            elif j == 6:
                # we'll manually adjust its value in the major-list, data_list, by +1 stone
                data_list[1] = data_list[1] + 1
                # continue adding +1 to our j value
                j = j + 1
                # and if the final stone of cup 2 is = 7 (hard programmed)
                if cup_2[1] + 2 == 7:
                    # first set cup 2 stone count to 0
                    cup_2[1] = 0
                    # then let that same player go again
                    return mancala_callout(print('Player has landed on a unique position. Please go again! '), data_list)
            # if the L-variable can still align to one of the numbers in remaining_bottom variable
            elif l in remaining_bottom:
                # starting from k = 8, we will keep adding + 1 stone to each cup that will be called upon
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase the k-iterator by + 1 to ensure each cup in the bottom row will get +1
                k = k + 1
                # increase the l-variable by +1 to ensure that have an even distribution of stones among the bottom cups
                l = l + 1
        # set cup 2 stone count = 0
        cup_2[1] = 0
        # return the major list of data
        return data_list


    # if cup 3 is chosen and its not empty
    elif cup_movement == '3' and cup_3[1] != 0:
        # set j = 3 to align with the remaining top cups
        j = 3
        # set k = 0 once again to help iterate through the bottom cups
        k = 0
        # l = 8 to help align with the bottom cups
        l = 8

        # the remaining cups for top cups portion
        remaining_top = [3, 4, 5, 6]
        # the remaining cups for the bottom cups portion
        remaining_bottom = [8, 9, 10, 11, 12, 13]


        # iterate as many times as there are stones in cup 3
        for i in range(cup_3[1]):
            # if j still aligns with the remaining_top list, but isn't j = 6, add +1 to each cup element in the top cups
            if j + 1 in remaining_top:
                top_cups[j][1] = top_cups[j][1] + 1
                # increase j by +1 to ensure that we won't give too many stones to the top cups only
                j = j + 1
            # if j = 6, add +1 to player 1 stone count
            elif j == 6:
                data_list[1] = data_list[1] + 1
                # increase j value to prevent giving too many stones to player one
                j = j + 1
            # if l aligns with bottom cups list, add +1 to each cup in the bottom row of cups
            elif l in remaining_bottom:
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to iterate through the bottom_cups list
                k = k + 1
                # increase l by +1 to ensure everything is aligning properly
                l = l + 1


        # set cup 3's stone count to 0
        cup_3[1] = 0
        # return the major data list
        return data_list
    elif cup_movement == '4' and cup_4[1] != 0:
        # set j = 3 to align with the remaining top cups
        j = 4
        # set k = 0 once again to help iterate through the bottom cups
        k = 0
        # l = 8 to help align with the bottom cups
        l = 8

        # the remaining cups for top cups portion
        remaining_top = [4, 5, 6]
        # the remaining cups for the bottom cups portion
        remaining_bottom = [8, 9, 10, 11, 12, 13]


        # iterate as many times as there are stones in cup 4
        for i in range(cup_4[1]):
            # if j still aligns with the remaining_top list, but isn't j = 6, add +1 to each cup element in the top cups
            if j + 1 in remaining_top:
                top_cups[j][1] = top_cups[j][1] + 1
                # increase j by +1 to ensure that we won't give too many stones to the top cups only
                j = j + 1
            # if j = 6, add +1 to player 1 stone count
            elif j == 6:
                data_list[1] = data_list[1] + 1
                # increase j value to prevent giving too many stones to player one
                j = j + 1
            # if l aligns with bottom cups list, add +1 to each cup in the bottom row of cups
            elif l in remaining_bottom:
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to iterate through the bottom_cups list
                k = k + 1
                # increase l by +1 to ensure everything is aligning properly
                l = l + 1


        # set cup 3's stone count to 0
        cup_4[1] = 0
        # return the major data list
        return data_list
    elif cup_movement == '5' and cup_5[1] != 0:
        # set j = 3 to align with the remaining top cups
        j = 5
        # set k = 0 once again to help iterate through the bottom cups
        k = 0
        # l = 8 to help align with the bottom cups
        l = 8

        # the remaining cups for top cups portion
        remaining_top = [5, 6]
        # the remaining cups for the bottom cups portion
        remaining_bottom = [8, 9, 10, 11, 12, 13]


        # iterate as many times as there are stones in cup 5
        for i in range(cup_5[1]):
            # if j still aligns with the remaining_top list, but isn't j = 6, add +1 to each cup element in the top cups
            if j + 1 in remaining_top:
                top_cups[j][1] = top_cups[j][1] + 1
                # increase j by +1 to ensure that we won't give too many stones to the top cups only
                j = j + 1
            # if j = 6, add +1 to player 1 stone count
            elif j == 6:
                data_list[1] = data_list[1] + 1
                # increase j value to prevent giving too many stones to player one
                j = j + 1
            # if l aligns with bottom cups list, add +1 to each cup in the bottom row of cups
            elif l in remaining_bottom:
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to iterate through the bottom_cups list
                k = k + 1
                # increase l by +1 to ensure everything is aligning properly
                l = l + 1


        # set cup 3's stone count to 0
        cup_5[1] = 0
        # return the major data list
        return data_list
    elif cup_movement == '6' and cup_6[1] != 0:
        # set j = 3 to align with the remaining top cups
        j = 6
        # set k = 0 once again to help iterate through the bottom cups
        k = 0
        # l = 8 to help align with the bottom cups
        l = 8

        # the remaining cups for top cups portion
        remaining_top = [6]
        # the remaining cups for the bottom cups portion
        remaining_bottom = [8, 9, 10, 11, 12, 13]


        # iterate as many times as there are stones in cup 6
        for i in range(cup_6[1]):
            # if j still aligns with the remaining_top list, but isn't j = 6, add +1 to each cup element in the top cups
            if j + 1 in remaining_top:
                top_cups[j][1] = top_cups[j][1] + 1
                # increase j by +1 to ensure that we won't give too many stones to the top cups only
                j = j + 1
            # if j = 6, add +1 to player 1 stone count
            elif j == 6:
                data_list[1] = data_list[1] + 1
                # increase j value to prevent giving too many stones to player one
                j = j + 1
            # if l is ever = 14, that means we will add +1 to player 2's cup
            elif l == 14:
                data_list[3] = data_list[3] + 1
                # set l back to 8 in case we need to ever come back to cup 8 ever again
                l = 8
            # if l aligns with bottom cups list, add +1 to each cup in the bottom row of cups
            elif l in remaining_bottom:
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to iterate through the bottom_cups list
                k = k + 1
                # increase l by +1 to ensure everything is aligning properly
                l = l + 1


        # set cup 3's stone count to 0
        cup_6[1] = 0
        # return the major data list
        return data_list
    elif cup_movement == '8' and cup_8[1] != 0:
        # a variable meant to see if it aligns with the top row of remaining cups
        j = 0
        # a variable meant to iterate through the bottom cup's list
        k = 0
        # set to 8 so we can begin giving each bottom cup +1 stone and not accidentally give them more than needed
        l = 8


        # remaining top cups list
        remaining_top = [1, 2, 3, 4, 5, 6]
        # remaining bottom cups list
        remaining_bottom = [8, 9, 10, 11, 12, 13]


        # iterate as many times as there are stones in cup 8
        for i in range(cup_8[1]):
            # if the variable l aligns with the bottom row of cups
            if l in remaining_bottom:
                # iterate through the bottom list according to k, and add +1 to that cup's stone count
                bottom_cups[k + 1][1] = bottom_cups[k + 1][1] + 1
                # increase k by +1
                k = k + 1
            # if j is ever = 6
            elif j == 6:
                # increase player 1's stone count by  +1
                data_list[1] = data_list[1] + 1
                # increase j value by +1 too to prevent more than one stone entering it at a time
                j = j + 1
            # if l is ever 14
            elif l == 14:
                # add +1 to player 2's stone count
                data_list[3] = data_list[3] + 1
                # reset l = 8 since now we are heading back into the top list of remaining cups!
                l = 8
            # and if j is ever in the remaining_top cups list (it aligns together)
            elif j in remaining_top:
                # add plus one to the cup in accordance to j
                top_cups[j][1] = top_cups[j][1] + 1
                # increase j by +1 to iterate through the top cups list more effectively
                j = j + 1


        # set cup 8 = 0
        cup_8[1] = 0
        # return our data list
        return data_list

    # if the player chooses cup 9 and its not empty
    elif cup_movement == '9' and cup_9[1] != 0:
        # set j = 0 to iterate through top list effectively
        j = 0
        # set k = 2 to iterate through the bottom list effectively
        k = 2
        # and set l = 9 to see if it aligns with the remaining bottom list
        l = 9


        # remaining top cups
        remaining_top = [1, 2, 3, 4, 5, 6]
        # remaining bottom cups
        remaining_bottom = [9, 10, 11, 12, 13]


        # iterate as many times as there are stones in cup 9
        for i in range(cup_9[1]):
            # if l + 1 still aligns in the remaining bottom list (which acts like a checker in a nutshell)
            if l + 1 in remaining_bottom:
                # add +1 to the next cup in our iteration through the bottom cups
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # iterate k by +1
                k = k + 1
                # increase l by +1 to ensure it will align properly
                l = l + 1
            # if j is ever 6
            elif j == 6:
                # add plus 1 to our player 1's stones
                data_list[1] = data_list[1] + 1
                # increase j by + 1 to prevent too many stones entering it
                j = j + 1
                # if cup 9 had 12 stones in it initially
                if cup_9[1] == 12:
                    # first set cup 9 to zero
                    cup_9[1] = 0
                    # let the player take another turn
                    return mancala_callout(print('Player has landed on a unique position. Please go again! '), data_list)
            # if l is ever 13
            elif l == 13:
                # increase player 2 stone count by +1
                data_list[3] = data_list[3] + 1
                # increase l by +1 to prevent too many stones being given to player 2
                l = l + 1
                # if cup 9 had 5 stones in it
                if cup_9[1] == 5:
                    # set cup 9 stones to 0
                    cup_9[1] = 0
                # let player take another turn
                return mancala_callout(print('Player has landed on a unique position. Please go again! '), data_list)
            # if more stones remain, start adding +1 to the remaining stones in the top portion of the remaining cups
            elif j in remaining_top:
                top_cups[j][1] = top_cups[j][1] + 1
                j = j + 1


        # set cup 9 to 0
        cup_9[1] = 0
        # return the data list
        return data_list

    # if cup 10 is selected and has stones in it
    elif cup_movement == '10' and cup_10[1] != 0:
        # set j = 1 to help align with the top portion of the remaining cups
        j = 1
        # set k = 3 to help iterate through the bottom portion of the cups
        k = 3
        # set l = 10 to help iterate through the remaining bottom list
        l = 10


        # list of remaining cups for the top portion
        remaining_top = [1, 2, 3, 4, 5, 6]
        # list of remaining cups for the bottom portion
        remaining_bottom = [10, 11, 12, 13]


        # iterate as many times as there are cups in cup 10
        for i in range(cup_10[1]):
            # if l + 1 still means our l is aligned OR inside the list of remaining bottom cups
            if l + 1 in remaining_bottom:
                # add +1 to each cup in the bottom portion of the cups
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to help iterate through the bottom cups list better
                k = k + 1
                # increase l by +1 to continue seeing whether we should add more stones to the bottom list of cups
                l = l + 1
            # if j = 6
            elif j == 6:
                # add +1 to player 1 stones
                data_list[1] = data_list[1] + 1
                # increase j + 1 to help see whether we need to add additional stones to the remaining top cups later on
                j = j + 1
            # if l is = 13
            elif l == 13:
                # that means we must add +1 stone to our player 2 list
                data_list[3] = data_list[3]+ 1
                # set l = 8
                l = 8
            # if j is in the remaining top list of cups
            elif j in remaining_top:
                # add +1 to each cup following the this formula. It may seem weird, but this was the only way it worked!
                top_cups[j - 1][1] = top_cups[j - 1][1] + 1
                # increase j by +1
                j = j + 1


        # set cup 10 stones to 0
        cup_10[1] = 0
        # finally, return the data list
        return data_list
    elif cup_movement == '11' and cup_11[1] != 0:
        # set j = 1 to help align with the top portion of the remaining cups
        j = 1
        # set k = 4 to help iterate through the bottom portion of the cups
        k = 4
        # set l = 11 to help iterate through the remaining bottom list
        l = 11

        # list of remaining cups for the top portion
        remaining_top = [1, 2, 3, 4, 5, 6]
        # list of remaining cups for the bottom portion
        remaining_bottom = [11, 12, 13]

        # iterate as many times as there are cups in cup 11
        for i in range(cup_11[1]):
            # if l + 1 still means our l is aligned OR inside the list of remaining bottom cups
            if l + 1 in remaining_bottom:
                # add +1 to each cup in the bottom portion of the cups
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to help iterate through the bottom cups list better
                k = k + 1
                # increase l by +1 to continue seeing whether we should add more stones to the bottom list of cups
                l = l + 1
            # if j = 6
            elif j == 6:
                # add +1 to player 1 stones
                data_list[1] = data_list[1] + 1
                # increase j + 1 to help see whether we need to add additional stones to the remaining top cups later on
                j = j + 1
            # if l is = 13
            elif l == 13:
                # that means we must add +1 stone to our player 2 list
                data_list[3] = data_list[3] + 1
                # set l = 8
                l = 8
            # if j is in the remaining top list of cups
            elif j in remaining_top:
                # add +1 to each cup following the this formula. It may seem weird, but this was the only way it worked!
                top_cups[j - 1][1] = top_cups[j - 1][1] + 1
                # increase j by +1
                j = j + 1

        # set cup 11 stones to 0
        cup_11[1] = 0
        # finally, return the data list
        return data_list
    elif cup_movement == '12' and cup_12[1] != 0:
        # set j = 1 to help align with the top portion of the remaining cups
        j = 1
        # set k = 4 to help iterate through the bottom portion of the cups
        k = 4
        # set l = 12 to help iterate through the remaining bottom list
        l = 12

        # list of remaining cups for the top portion
        remaining_top = [1, 2, 3, 4, 5, 6]
        # list of remaining cups for the bottom portion
        remaining_bottom = [12, 13]

        # iterate as many times as there are cups in cup 11
        for i in range(cup_12[1]):
            # if l + 1 still means our l is aligned OR inside the list of remaining bottom cups
            if l + 1 in remaining_bottom:
                # add +1 to each cup in the bottom portion of the cups
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to help iterate through the bottom cups list better
                k = k + 1
                # increase l by +1 to continue seeing whether we should add more stones to the bottom list of cups
                l = l + 1
            # if l is = 13
            elif l == 13:
                # that means we must add +1 stone to our player 2 list
                data_list[3] = data_list[3] + 1
                # set l = 8
                l = 8
            # if j is in the remaining top list of cups
            elif j in remaining_top:
                # add +1 to each cup following the this formula. It may seem weird, but this was the only way it worked!
                top_cups[j - 1][1] = top_cups[j - 1][1] + 1
                # increase j by +1
                j = j + 1
                # if j = 6
            elif j == 6:
                # add +1 to player 1 stones
                data_list[1] = data_list[1] + 1
                # increase j + 1 to help see whether we need to add additional stones to the remaining top cups later on
                j = j + 1

        # set cup 12 stones to 0
        cup_12[1] = 0
        # finally, return the data list
        return data_list
    elif cup_movement == '13' and cup_13[1] != 0:
        # set j = 1 to help align with the top portion of the remaining cups
        j = 1
        # set k = 4 to help iterate through the bottom portion of the cups
        k = 5
        # set l = 12 to help iterate through the remaining bottom list
        l = 13

        # list of remaining cups for the top portion
        remaining_top = [1, 2, 3, 4, 5, 6]
        # list of remaining cups for the bottom portion
        remaining_bottom = [13]

        # iterate as many times as there are cups in cup 13
        for i in range(cup_13[1]):
            # if l + 1 still means our l is aligned OR inside the list of remaining bottom cups
            if l + 1 in remaining_bottom:
                # add +1 to each cup in the bottom portion of the cups
                bottom_cups[k][1] = bottom_cups[k][1] + 1
                # increase k by +1 to help iterate through the bottom cups list better
                k = k + 1
                # increase l by +1 to continue seeing whether we should add more stones to the bottom list of cups
                l = l + 1
            # if j = 6
            elif j == 6:
                # add +1 to player 1 stones
                data_list[1] = data_list[1] + 1
                # increase j + 1 to help see whether we need to add additional stones to the remaining top cups later on
                j = j + 1
            # if l is = 13
            elif l == 14:
                # that means we must add +1 stone to our player 2 list
                data_list[3] = data_list[3] + 1
                # set l = 8
                l = 8
            # if j is in the remaining top list of cups
            elif j in remaining_top:
                # add +1 to each cup following the this formula. It may seem weird, but this was the only way it worked!
                top_cups[j - 1][1] = top_cups[j - 1][1] + 1
                # increase j by +1
                j = j + 1

        # set cup 13 stones to 0
        cup_13[1] = 0
        # finally, return the data list
        return data_list

    # if you make the wrong call out, then call again,
    else:
        mancala_callout(cup_movement, data_list)


"""
This marks the end of the functions needed for the project
"""
# main block of code


if __name__ == '__main__':
    # asking user for whether they want to play the game or not
    opening_feedback = input('Hello there! Would you like to play the Mancala game? (y/n) ').lower()
    # checking to see if user made proper inputs
    if opening_feedback != 'y' or opening_feedback != 'n':
        opening_feedback = input('Hello there! Would you like to play the Mancala game? (y/n) ').lower()

    while opening_feedback != 'n':


        # creating an empty list of players
        list_of_players = []
        # creating an empty string variable that will be our player 1
        player_a = ''
        # creating an empty string variable that will be our player 2
        player_b = ''
        # calling our function, get_players() to get a list of of our player names
        get_players()
        # splitting the list into the once-empty string variables I made earlier
        for i in range(len(list_of_players)):
            if i == 0:
                player_a = list_of_players[0]
            else:
                player_b = list_of_players[1]
        """
        This will mark the end of getting the players
        """

        # creating an empty list for the mancala_board
        mancala_board = []
        # creating a variable that signals what each cup will start with- 4 stones in this case!
        stones = 4

        # assigning each player with 0 stones in their cups
        mancala_stone_a = 0
        # assigning each player with 0 stones in their cups
        mancala_stone_b = 0

        # creating a list for each of the cups. This is to really make sure that there is no confusion, and our player
        # is aware of the names of each list that is assigned to each cup
        cup_1 = ['cup 1', stones]
        cup_2 = ['Cup 2', stones]
        cup_3 = ['Cup 3', stones]
        cup_4 = ['Cup 4', stones]
        cup_5 = ['Cup 5', stones]
        cup_6 = ['Cup 6', stones]
        cup_8 = ['Cup 8', stones]
        cup_9 = ['Cup 9', stones]
        cup_10 = ['Cup 10', stones]
        cup_11 = ['Cup 11', stones]
        cup_12 = ['Cup 12', stones]
        cup_13 = ['Cup 13', stones]


        # creating a list that will have each sublist within them according to their respective parts. This is top cups
        top_cups = [cup_1, cup_2, cup_3, cup_4, cup_5, cup_6]
        # creating another list that will have each sublist within them- this is the bottom cups list
        bottom_cups = [cup_8, cup_9, cup_10, cup_11, cup_12, cup_13]

        # a checker to later ensure if our player is making reasonable callouts for the top cups
        top_cups_checker = ['cup_1', 'cup_2', 'cup_3', 'cup_4', 'cup_5', 'cup_6']
        # another checker to later ensure if our player is making reasonable callouts for the bottom cups
        bottom_cups_checker = ['cup_8', 'cup_9', 'cup_10', 'cup_11', 'cup_12', 'cup_13']

        # each time we play this game, our initial cup_selection will be empty so the player can make an accurate call
        cup_selection = ''

        # resetting every time we play this game the empty counters as explained in the play_game function
        empty_counter_top = 0
        # still resetting the counters ever time we play this game as explained in the play_game or
        # manacala_data_checker function
        empty_counter_bottom = 0

        # creating a major list that will have all of the previous lists and/or variables stored for data transfer
        data_list = [top_cups, mancala_stone_a, bottom_cups, mancala_stone_b]
        # creating another list that will store the data of the mancala stones
        mancala_list = [mancala_stone_a, mancala_stone_b]

        # and now, we will run the game!
        run_game(empty_counter_top, empty_counter_bottom)


        # once the game is over... we will once again ask the player if they would love to play the game again!
        opening_feedback = input('Hello there! Would you like to play the Mancala game? (y/n) ').lower()
