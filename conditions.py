from methods import set_value_and_delete_it_from_areas

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
            set_value_and_delete_it_from_areas(box, list_of_all_areas, box.possible_values[0])
            process = True
    return process


def condition2(list_of_all_areas, symbols_to_fill):
    '''
    zjistim, zda a ktere cislo se da vepsat prave a jen na jedno misto
    :param area:
    :return: to teprve uvidime, co budeme potrebovat
    '''
    process = False
    for area in list_of_all_areas:
        for i in symbols_to_fill:
            print(i)
            if sum([box.possible_values.count(i) for box in area.field]) == 1:
                for j in area.field:
                    if i in j.possible_values:
                        box = j
                set_value_and_delete_it_from_areas(box, list_of_all_areas, i)
                process = True
    return process
