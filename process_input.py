from objects.box import Box
from objects.field import Field
from objects.area import Area
from objects.areas_collections import AllAreas

def nacti_symbols_to_fill(vstup1):
    with open(vstup1) as f:
        for line in f:
            symbols_to_fill = line.strip().split()
    return symbols_to_fill


def nacti_field(field, vstup2, symbols_to_fill): #vytvori pole a cisla zapise jako prazdne pole s jedinou poss_value
    with open(vstup2) as f:
        for line in f:
            new_line = line.strip().split()
            for i in new_line:
                new_box = Box(symbols_to_fill)
                if i in symbols_to_fill:
                    new_box.possible_values = [i]
                field.field.append(new_box)


def nacti_areas(field, vstup3, all_areas):
    with open(vstup3) as f:
        new_list = []
        for line in f:
            if line != '\n':
                new_list += line.strip().split()
            elif new_list:
                actual_set_of_areas = make_dict(new_list, field)
                for i in actual_set_of_areas.keys():
                    new_area = Area(actual_set_of_areas[i], symbols_to_fill=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
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


def initialize(vstup1, vstup2, vstup3):
    symbols_to_fill = vstup1
    field = Field()
    nacti_field(field, vstup2, symbols_to_fill)
    all_areas = AllAreas()
    nacti_areas(field, vstup3, all_areas)
    return field, all_areas

    #mame vyplnene pole a vsechny areas v all_areas










