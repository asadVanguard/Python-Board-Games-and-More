import json


def recursion(useful, object, found):



    for i in range(len(object[1])):
        if useful in object[1][i]:
            found += 1
            print(found)
        elif object[1][i][0] == Si or object[1][i][0] == Fe or object[1][i][0] == Cu or object[1][i][0] == Pl and object[1][i][0] != useful:
            print('Skipped since not useful')
        else:




            recursion(Fe, data['recipes'][object[1][i][0]][1], found)
    return found + 1


def read_json():
    read_file = open('test.json', 'r')
    # just  string with the json stuff read in
    json_string = read_file.read()
    # just call read once, get everything out of the file.
    data = json.loads(json_string)

    return data


if __name__ == '__main__':

    Fe = 'iron'
    Si = 'silicon'
    Pl = 'plastics'
    Cu = 'copper'

    found = 0


    data = read_json()
    print(data)


    # print(data['recipes']['factory'][1])
    amount_of_si = recursion(Fe, data['recipes']['mine'][1], found)



    print(data['recipes']['factory'][1][1][1][1])

