"""
File:   recipe.py
Author:  Asad Siddiqui
Date:    4/30/2021
Section: Section 35, Wednesday 11 AM
E-mail:  asiddiq3@umbc.edu
Description:
"""
# main block of code

if __name__ == '__main__':
    import json
    # raw material dictionary
    raw_material_dict = {}
    # factory dictionary
    factory_output_dict = {}
    # the finalized dictionary that will be comprised of both previous, smaller dictionaries
    my_recipe_dict = {}  # finalized dictionary
    # telling the user to input the name of the raw material they wanna put in
    raw_material_generator = input('Name the raw material: ')

    # until they say done, keep adding more raw materials to the raw material dictionary!
    while raw_material_generator != 'done':
        raw_material_generator_rate = int(input('What is the rate at which it is mined? '))

        raw_material_dict[raw_material_generator] = raw_material_generator_rate

        raw_material_generator = input('Name the next raw material: ')

    # creating a parts list that will store the parts needed for the crafting book
    parts = []
    # asking user to tell us the output of the factory- one of them at least
    factory_output_generator = input('Name the output: ')
    # until the user says done, keep adding more outputs to the dictionary
    while factory_output_generator != 'done':
        # every time, reset the parts list, and add fresh output materials to them!
        parts = []
        # the rate at which it is output is needed in case
        factory_output_generator_rate = int(input('What is the rate at which it is output? '))
        # telling the user to name at least 1 ingredient needed for this
        factory_output_ingredient_name = input('Name the ingredient needed for this, or say stop if no ingredients '
                                           'are needed: ')
        # until the user tells says stop, keep adding more ingredients for that respective output the factory will make
        while factory_output_ingredient_name != 'stop':
            # ask user how much of that ingredient is needed
            factory_output_ingredient_amount = int(input('How much of that ingredient is needed? '))
            # create a tuple that houses the ingredient name and the input needed to make the output and append to parts
            # list
            parts.append((factory_output_ingredient_name, factory_output_ingredient_amount))
            # asking the user for any more ingredients needed for this output to work
            factory_output_ingredient_name = input('Any more ingredients needed for this output? Say stop to not '
                                                   'add anymore ingredients. ')

        # after the iteration is over, we will simply display the newly, completely finished output dictionary
        factory_output_dict[factory_output_generator] = [('Output:', factory_output_generator,
                                                          'Output_Count:', factory_output_generator_rate),
                                                         ('Parts:', parts)]

        # asking user to input another output, or hit done to leave the program
        factory_output_generator = input('Name the next output or done to be finished: ')

    # creating the ultimate, big crafting book dictionary that will now be converted into a JSON file
    my_recipe_dict = {'raw_materials': raw_material_dict, 'recipes': factory_output_dict}

    # creating file called craftingBook.json in which we will write all over the file
    write_json_file = open('craftingBook.json', 'w')
    # using the JSON import, we will dump the dictionary into a variable
    string_to_write = json.dumps(my_recipe_dict)
    # then write the file using said variable
    write_json_file.write(string_to_write)
    # finally, close the file so that it does cause corruption to the file.
    write_json_file.close()
