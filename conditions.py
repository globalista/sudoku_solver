def condition1(field, all_areas):
    '''
    projde pole a  pokud je nekde jedina poss_value, zapise ji a vyskrta v prislusnych areas
    :param field:
    :param list_of_all_areas:
    :return: True if process or False
    '''
    process = False
    for box in field.field:
        if len(box.possible_values) == 1:
            all_areas.set_value_and_delete_it_from_areas(box, box.possible_values[0])
            process = True
    return process


def condition2(all_areas, symbols_to_fill):
    '''
    zjistim, zda a ktere cislo se da vepsat prave a jen na jedno misto
    :param area:
    :return: to teprve uvidime, co budeme potrebovat
    '''
    process = False
    for area in all_areas.list_of_all_areas:
        for i in symbols_to_fill:
            if sum([box.possible_values.count(i) for box in area]) == 1:
                for j in area:
                    if i in j.possible_values:
                        box = j
                all_areas.set_value_and_delete_it_from_areas(box, i)
                process = True

    return process
