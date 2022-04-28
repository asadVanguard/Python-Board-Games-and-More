"""
File:   silicon_crisis.py
Author:  Asad Siddiqui
Date:    4/30/2021
Section: Section 35, Wednesday 11 AM
E-mail:  asiddiq3@umbc.edu
Description: This is almost like a Minecraft Simulator, except with many modified parts.
"""
# importing the JSON program
import json


# first class being made: Mine class
class Mine:
    def __init__(self, name, status_calamitous):
        # the constructor is mostly meant to extract the name of the mine
        self.name = name
        # the other thing is what is the status of the mine- is it mining iron, or copper, for example.
        self.mine_status = status_calamitous

    # creating first Mine - method
    def set_mine(self, number, raw_material):
        """
        The goal is to set the mines to a certain raw_material

        :param number: the number of the mine set to a location
        :param raw_material: the raw_material that needs to be mined
        :return: how much material it has collected over time
        """
        # central command is the original input divided into a list. Algorithm reqs. a number specified
        if central_command_breakdown[2] == '0':
            # if '0' was the number following 'mine', we will alter the status of Mine 0 mostly.
            mine_0.mine_status = raw_material
            # return the status of mine_0's name, and mine_0's status of what it's mining.
            return mine_0.name, mine_0.mine_status
        # if we select mine_1
        elif central_command_breakdown[2] == '1':
            # setting its status to the raw material needed
            mine_1.mine_status = raw_material
            # return the results of setting up the object, mine_1
            return mine_1.name, mine_1.mine_status
        # if we select mine_2
        elif central_command_breakdown[2] == '2':
            # granted we craft another mine, we will set its status to the material needed
            mine_2.mine_status = raw_material
            # returning the results of said new object
            return mine_2.name, mine_2.mine_status

    # final method for the Mine class
    def display_mines(self):
        """
        Display the mine status and what it's mining.
        :return: how much it's outputting per turn
        """
        # meaning, if we don't set up mine_0
        if mine_0.mine_status == '':
            # we will return a modified statement which says that one in particular is closed
            return print('Mine 0' + '\n' + 'currently inactive.' + '\n' +
                         mine_1.name + '\n' + '{}'.format(mine_1.mine_status) + ' mine producing 5 per turn.')
        # if we don't set up mine_1
        elif mine_1.mine_status == '':
            # likewise, for mine_1, the same will follow!
            return print(mine_0.name + '\n' + '{}'.format(mine_0.mine_status) + ' mine producing 5 per turn' + '\n' +
                        'Mine 1' + '\n'  + 'currently inactive.')
        # otherwise, we will print out the full statement of mine statuses
        else:
            return print(mine_0.name + '\n' + '{}'.format(mine_0.mine_status) + ' mine producing 5 per turn.' + '\n' +
                         mine_1.name + '\n' + '{}'.format(mine_1.mine_status) + ' mine producing 5 per turn.')

# ----------------------------- Comment Barrier -------------------------------------------------------------------


# creating another class: Factory
class Factory:
    def __init__(self, name, status_calamitous):
        # the name of the factory is the number of the factory
        self.factory_number = name
        # factory status will be adjusted the sme way the mine status was
        self.factory_status = status_calamitous

    # first method of the class
    def set_factory(self, number, status_altercation):
        """
        Sets the factory to a certain mode, and allows changes with the recipe
        :param number: the factory number
        :param status_altercation: sets to another recipe as needed
        :return:
        """
        # alter the factory_0's status if declared to what we need to produce
        if central_command_breakdown[2] == '0':
            factory_0.factory_status = status_altercation
            # return factory_0's status afterwards
            return factory_0.factory_number, factory_0.factory_status
        # alter factory_1's status if ever declared
        elif central_command_breakdown[2] == '1':
            factory_1.factory_status = status_altercation
            # return factory_1 afterwards
            return factory_1.factory_number, factory_1.factory_status

    def display_factories(self):
        """
        Simply going to display the status of the factories. Nothing much more to this
        :return: The factory status' and what they will be doing every turn
        """

        print('Status: Calamitous')


# ----------------------------- Comment Barrier -------------------------------------------------------------------

# display function. Not class locked since we will need this for all purposes from here on forth
def display():
    """
    Simple function. No input required- regardless of what they need, this will display everything accordingly.
    Universal and is NOT class-locked, aka a Method.
    """
    # essentially, if the user wants to display the raw materials that are possible to obtain,
    if central_command_breakdown[1] == 'raw' and central_command_breakdown[2] == 'materials':
        # print the header first
        print(':::Current List of Raw Materials:::')
        for i in range(len(raw_materials)):
            # then print all of the possible raw materials to obtain
            print('{}'.format(raw_materials[i][0]))

    # if they want to see the stockpile,
    elif central_command_breakdown[1] == 'stockpile':
        # print out the header first
        print(':::Current Stockpile:::')
        for i in range(len(raw_materials)):
            # and then print out the list of materials, plus how much of each raw material is left over
            print('{}:'.format(raw_materials[i][0]) + ' {}'.format(raw_materials[i][1]))

        for i in range(len(factory_related)):
            # this will also include the number of products available.
            print('{}'.format(factory_related[i][0]) + ' {}'.format(factory_related[i][1]))

    # if they want to see the crafting book
    elif central_command_breakdown[1] == 'recipes':
        # print out the header first
        print(':::Current Recipe Book:::')
        # and then print out the dictionary full of recipes
        print(data['recipes'])

    return ''


# another function that is universal and is not locked behind as a class method- this one is very crucial
def end_turn(turn_counter, raw_materials, factory_related, list_of_mines, list_of_factories):
    """
    This will initiate ending the turn, and go to the next phase.
    :param turn_counter: a counter that keeps track of turns gone by
    :param raw_materials: the list of raw materials that will be kept track of regardless of what may happen
    :param factory_related: the list of factory-related things that will be kept track of between phases.
    :param list_of_mines: a list of mines to permit easier time translating
    :param list_of_factories: a list of factories
    :return: The new list of materials potentially generated from the mines, alongside any conversions if necessary.
    """
    # increasing our turn counter by +1
    turn_counter += 1
    # iterate as many times as there are mines that are active
    for i in range(len(list_of_mines)):
        # burning through the list of mines, and what exactly each is mining every time we iterate through the list
        material_being_mined = list_of_mines[i]

        # if a mine is mining iron,
        if material_being_mined == 'iron':
            # modify the list that is associated with iron's num by the amount being mined according to JSON file
            iron[1] = iron[1] + data['raw_materials']['iron']
        # likewise, if a mine is mining silicon
        elif material_being_mined == 'silicon':
            # modify the list that is associated with silicon's num by the amount being mined according to the JSON file
            silicon[1] = silicon[1] + data['raw_materials']['silicon']
        # likewise, if a mine is mining copper
        elif material_being_mined == 'copper':
            # modify the list that is associated with copper's num by the amount being mined according to the JSON file.
            copper[1] = copper[1] + data['raw_materials']['copper']
        # likewise, if a mine is mining plastics
        elif material_being_mined == 'plastics':
            # modify the list that is associated with plastic's num by the amount being mined according to the JSON file
            plastics[1] = plastics[1] + 1  # alter these values

    # iterate as many times as there are factories activated and running
    for i in range(len(list_of_factories)):
        # each time we iterate, try to possibly craft something the factories want crafting for
        factory_status_this_phase = list_of_factories[i]

        # so if any factory is set to factory mode,
        if factory_status_this_phase == 'factory':
            # and the amount of iron and cogs are greater than or equal to the required amount,
            if iron[1] >= data['recipes']['factory'][1][1][0][1] and cogs[1] >= data['recipes']['factory'][1][1][1][1]:
                # increase the num of factories available by +1
                factory_available[1] = factory_available[1] + 1
                # and now subtract the number of iron from amount needed to create a factory in the first place
                iron[1] = iron[1] - data['recipes']['factory'][1][1][0][1]
                # and now also subtract the number of cogs needed to create to create a factory in the first place too
                cogs[1] = cogs[1] - data['recipes']['factory'][1][1][1][1]

        # if any factory is set to cog creation mode
        elif factory_status_this_phase == 'cog':
            # and the amount of iron is >= to the amount needed to make one according to the JSON file
            if iron[1] >= data['recipes']['cog'][1][1][0][1]:
                # increase the amount of cogs by +1
                cogs[1] = cogs[1] + 1
                # and subtract the amount of iron needed to create a cog in the first place
                iron[1] = iron[1] - data['recipes']['cog'][1][1][0][1]
        # if any factory is set to creating another mine
        elif factory_status_this_phase == 'mine':
            # and the number of iron and cogs are greater than or equal to the amount needed to create a mine
            if iron[1] >= data['recipes']['mine'][1][1][0][1] and cogs[1] >= data['recipes']['mine'][1][1][1][1]:
                # modify the list by essentially stating one more mine is officially ready for use
                mines_additional[1] = mines_additional[1] + 1
                # and subtract the amount of iron to create a mine in the first place
                iron[1] = iron[1] - data['recipes']['mine'][1][1][0][1]
                # and also subtract the amount of cogs needed to create a mine in the first place too
                cogs[1] = cogs[1] - data['recipes']['mine'][1][1][1][1]

    print('We are now proceeding to the next turn')

    return factory_available, cogs, raw_materials, plastics, turn_counter


# another fucntion that is meant to reveal how much of X is in Y
def how_much(useful, object, found):
    """
    This is a basic recursive function that will reveal how many times you will need X to make Y.
    The big difference is that this will not display exactly how many of X is needed, but rather how
    many times X was spotted in the making of Y.
    :param useful: The X, or what we will need
    :param object: The Y, or what we are creating
    :param found: how many times X has been spotted in creating Y.
    :return: The number of times X has been spotted in creating Y.
    ---> so if factorys are made of cogs and iron, and cogs are made of iron, that would be mean we would
    return the value of 2 since we needed 2 piles of iron to make one factory!
    """

    # so we will always iterate through the length of the dictionary key value, however, focusing on
    # second list made.
    for i in range(len(object[1])):
        # useful in the object's 1 creation inventory (parts)
        if useful in object[1][i]:
            # increase found by +1
            found += 1
        # if it's a raw material, but not the one we were looking for,
        elif object[1][i][0] == Si or object[1][i][0] == Fe or object[1][i][0] == Cu or object[1][i][0] == Pl and object[1][i][0] != useful:
            # skipping it and moving onto the next part component of the object or Y needed
            print('Skipped since not useful')
        # essentially, if it's not one of the raw materials directly listed as a part initially, recursive case
        else:
            # begin recursion by diving into parts of one of the parts needed.
            how_much(Fe, data['recipes'][object[1][i][0]][1], found)
    # return found by + 1
    return found + 1


# final function needed for this to work
def read_json(read_file):
    """
    The goal is to extract the crafting book recipes from the file given
    :param read_file: The crafting book
    :return: a new dictionary full of terms.
    """
    # setting a variable equal to the file we are just about to open up
    read_data = open(read_file, 'r')
    # just  string with the json stuff read in
    json_string = read_data.read()
    # just call read once, get everything out of the file.
    data = json.loads(json_string)
    # return new data aka the dictionary
    return data


# main block of code

if __name__ == '__main__':
    # telling user to input the SC file name to continue.
    read_file = input('Enter SC Recipe File Name: ')

    # data is the dictionary made and extracted from the JSON file
    data = read_json(read_file)

    # setting up 4 different elements, and lists to go with them. 0 is alterable since that will be adjusted
    # between rounds
    iron = ['iron', 0]
    copper = ['copper', 0]
    silicon = ['silicon', 0]
    plastics = ['plastics', 0]

    # number of factories set up
    factory = 0
    # number of factories active now - two by default since you are given two at the start
    factory_available = ['Factories Active', 2]
    # number of cogs, and a list to be associated so it can work between functions and main code
    cogs = ['Cogs', 0]
    # number of circuits, and a list to be associated so it can work between functions and main code
    circuit = ['circuit', 0]
    # number of ADDITIONAL mines being made. As time passes on, once again, we might fight ourselves needing more mines
    mines_additional = ['mines', 0]

    # list of raw materials
    raw_materials = [iron, copper, silicon, plastics]
    # a small list that will include the number of factories available, and as well as the list of products possible
    factory_related = [factory_available, cogs, circuit, mines_additional]

    # a turn counter to keep track of how many days went by
    turn_counter = 0

    # central command is the main action the user will input
    central_command = input('Select Next Action>> ')

    # while the user does not respond with quit, we will keep going with this program/playing the game
    while central_command != 'quit':
        # splitting the command given into a list to help interpret it a lot easier
        central_command_breakdown = central_command.split(" ")

        # if we are setting up the mines
        if central_command_breakdown[0] == 'set' and central_command_breakdown[1] == 'mine':
            # if we are setting up mine_0
            if central_command_breakdown[2] == '0':
                # first create the object
                mine_0 = Mine('Mine 0', '')
                # then assign a variable to the raw material needed
                raw_material_demanded = central_command_breakdown[3]
                # finally, call the class-specific method to set up the mines properly (assigning raw mat. to them)
                mine_0.set_mine(0, raw_material_demanded)
                # increase the number of mines by +1

            # if we are focusing on mine_1
            elif central_command_breakdown[2] == '1':
                # first create the object
                mine_1 = Mine('Mine 1', '')
                # then assign a variable to the raw material needed
                raw_material_demanded = central_command_breakdown[3]
                # finally, call the class-specific method to set up the mines properly (assigning raw mat. to them)
                mine_1.set_mine(1, raw_material_demanded)
                # increase the number of mines by +1

            # more than likely, we will never exceed having 3 mines in total.
            elif central_command_breakdown[2] == '2' and mines_additional[1] > 0 :
                # first create the object
                mine_2 = Mine('Mine 2', '')
                # then assign a variable to the raw material needed
                raw_material_demanded = central_command_breakdown[3]
                # finally, call the class-specific method to set up the mines properly (assigning raw mat. to them)
                mine_2.set_mine(2, raw_material_demanded)
                # increase the number of mines by +1

        # if the user wants to display the mines and what rate they are mining at,
        elif central_command_breakdown[0] == 'display' and central_command_breakdown[1] == 'mines':
            # any mine is needed, as it will not matter since every mine will ideally be shown anyway!
            mine_0.display_mines()

        # another command for setting up the factories
        elif central_command_breakdown[0] == 'set' and central_command_breakdown[1] == 'factory':
            # setting up factory 0
            if central_command_breakdown[2] == '0':
                # first create the object
                factory_0 = Factory('Factory 0', '')
                # set a variable equal to the product we desire
                factory_status_altercation = central_command_breakdown[3]
                # then alter the new object so that it will work towards creating the object between turns
                factory_0.set_factory(0, factory_status_altercation)
                # increase number of factories being used by +1
                factory += 1

            # setting up factory 1
            elif central_command_breakdown[2] == '1':
                # first create the object
                factory_1 = Factory('Factory 1', '')
                # set a variable equal to the product we desire
                factory_status_altercation = central_command_breakdown[3]
                # then alter the new object so that it will work towards creating the object between turns
                factory_1.set_factory(1, factory_status_altercation)
                # increase number of factories being used by +1
                factory += 1

            # setting up factory 2 once created from the end_turn function
            elif factory > 2:
                # first create the object
                factory_2 = Factory('Factory 1', '')
                # set a variable equal to the product we desire
                factory_status_altercation = central_command_breakdown[3]
                # then alter the new object so that it will work towards creating the object between turns
                factory_2.set_factory(2, factory_status_altercation)
                # increase number of factories being used by +1
                factory += 1

        # if the user wants to display the amount of raw materials or stuff in the stockpile,
        elif central_command_breakdown[0] == 'display' and (central_command_breakdown[1] == 'raw' or
                                                            central_command_breakdown[1] == 'stockpile' or
                                                            central_command_breakdown[1] == 'recipes'):
            # simply display the what is needed. No extra inputs needed since everything was placed into a list!
            print(display())

        # command to finally move onto the next day
        elif central_command_breakdown[0] == 'end' and central_command_breakdown[1] == 'turn':
            # list of factories made and set to be active
            list_of_factories = []
            # list of mines made and set to be active (both are empty at this time)
            list_of_mines = []
            # if the number of factories set up was less than or equal two
            if factory < 2:
                list_of_factories.append(factory_0.factory_status)
            elif factory == 2:
                # adding factory 1 and 2's statuses to our empty list
                list_of_factories.append(factory_0.factory_status)
                list_of_factories.append(factory_1.factory_status)
            # if not, we will add all 3 factories to our factory list!
            else:
                list_of_factories = [factory_0.factory_status, factory_1.factory_status, factory_2.factory_status]

            # then, adding mine 0 and 1's statuses to the list of mines just created
            list_of_mines.append(mine_0.mine_status)
            list_of_mines.append(mine_1.mine_status)
            # if we so happen to create another mine
            if mines_additional[1] > 2:
                # meaning, mine 2 is now active, add it into this too.
                list_of_mines.append(mine_2.mine_status)
            # end turn means that we will offically take the big list of everything we have, and modify their respective
            # numbers
            end_turn(turn_counter, raw_materials, factory_related, list_of_mines, list_of_factories)

            # finally, print out what turn it is to the user.
            print('It is now turn {}.'.format(turn_counter))

        # if the user wants to use the basic recursion protocol
        elif central_command_breakdown[0] == 'how' and central_command_breakdown[1] == 'many':
            # set x to whatever the 3rd word was when commanded
            x = central_command_breakdown[3]
            # set y to whatever the 7th word was when commanded
            y = central_command_breakdown[7]

            # 4 variables were made for the sake of making the recursive function work a little better and faster
            Fe = 'iron'
            Si = 'silicon'
            Pl = 'plastics'
            Cu = 'copper'
            # the 4 variables above were simple so that it can help the accuracy of the recursive function out

            # creating another variable, found, that will represent the number of times X has appeared in Y
            found = 0

            # data is the dictionary made and extracted from the JSON file
            data = read_json(read_file)

            print(data)

            # this is the exact ratio needed really to make things work out. Not the best of the best, but it works
            print(x, data['recipes'][y][1])
            amount_of_object = how_much(x, data['recipes'][y][1], found)

            print(amount_of_object)

        # last but not least, if a command was messed up partially, repeat it
        else:
            print('Command error- try again')

        central_command = input('Select Next Action>> ')

    print('Goodbye! Have a wonderful day!')












