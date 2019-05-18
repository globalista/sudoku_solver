from objects.field import Field
from objects.areas_collections import AllAreas


def upload_symbols_to_fill(vstup1):
    with open(vstup1) as f:
        for line in f:
            symbols_to_fill = line.strip().split()
    return symbols_to_fill


def make_a_list_of_requested_values(vstup2):
    with open(vstup2) as f:
        list_of_req_vals = []
        for line in f:
            list_of_req_vals += line.strip().split()
    return list_of_req_vals


def upload_requested_values(field, vstup2, areas, symbols_to_fill):
    list_of_req_vals = make_a_list_of_requested_values(vstup2)
    if len(list_of_req_vals) != len(field.field):
        raise IndexError('Zadani neodpovida velikosti pole')
    for i, j in zip(list_of_req_vals, field.field):
        if i in symbols_to_fill:
            areas.set_value_and_delete_it_from_areas(j, i)


def upload_areas(field, vstup3, all_areas):
    with open(vstup3) as f:
        new_list = []
        for line in f:
            if line != '\n':
                new_list += line.strip().split()
            elif new_list:
                actual_set_of_areas = make_dict(new_list, field)
                for i in actual_set_of_areas.keys():
                    # new_area = Area(actual_set_of_areas[i], ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                    new_area = actual_set_of_areas[i]
                    all_areas.add_area(new_area)
                new_list = []


def make_dict(list, field):
    n = len(field.field)
    if len(list) != n:
        raise ValueError('zadane oblasti nekoresponduji se zakladnim zadanim', n, len(list), list)
    new_dict = {}
    for i in range(n):
        tohle = list[i]
        if tohle.isalnum():
            if tohle in new_dict.keys():
                new_dict[tohle] += [field.field[i]]
            else:
                new_dict[tohle] = [field.field[i]]
    return new_dict


def initialize(vstup1, vstup2, vstup3, n):
    symbols_to_fill = vstup1
    field = Field(n, symbols_to_fill)
    # nacti_field(field, vstup2, symbols_to_fill)
    all_areas = AllAreas()
    upload_areas(field, vstup3, all_areas)
    upload_requested_values(field, vstup2, all_areas, symbols_to_fill)
    return field, all_areas

    # mame vyplnene pole a vsechny areas v all_areas










