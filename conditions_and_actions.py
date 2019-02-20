def areas_containing_the_box(box, list_of_all_areas):
    '''
    make list of areas containing the box
    :param box:
    :param list_of_all_areas:
    :return: list of areas containing the box
    '''
    areas_containing = []
    for area in list_of_all_areas:
        if box in area.field:
            areas_containing.append(area)
    return areas_containing

def set_value_and_delete_it_from_areas(box, list_of_all_areas, value):
    '''
    :param box:
    :param list_of_all_areas:
    :param value:
    :return: set value to the box and delete the value in all other areas containing
    '''
    box.set_value(value)
    for area in areas_containing_the_box(box, list_of_all_areas):
        area.remove_from_possible_values(value)


def condition1(field, list_of_all_areas):
    '''
    projde pole a  pokud je nekde jedina poss_value, zapise ji a vyskrta v prislusnych areas
    :param field:
    :param list_of_all_areas:
    :return: True if process or False
    '''
    process = False
    for box in field.field:
        if len(box.possible_values) == 1:
            set_value_and_delete_it_from_areas(list_of_all_areas, box, box.possible_values[0])
            process = True
    return process


def condition2(list_of_all_areas):
    '''
    zjistim, zda a ktere cislo se da vepsat prave a jen na jedno misto
    :param area:
    :return: to teprve uvidime, co budeme potrebovat
    '''
    process = False
    for area in list_of_all_areas:
        for i in area.nums_to_fill:
            if sum([box.possible_values.count(i) for box in area]) == 1:
                set_value_and_delete_it_from_areas(list_of_all_areas, box, i)
                process = True
    return process
