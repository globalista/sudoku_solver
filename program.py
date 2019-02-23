from objects import Field, Area
from areas_settings import areas_coords
from conditions import condition1, condition2
from solver import solver
from methods import input_to_matrix, load_input


if __name__ == '__main__':
    field = Field()
    list_of_all_areas = []
    for list_of_coords in areas_coords:
        new_area = Area(list_of_coords, field)
        list_of_all_areas.append(new_area)
    matrix = input_to_matrix('vstup')
    load_input(field, matrix, list_of_all_areas)
    field.print9x9()
    solver(field, list_of_all_areas, condition1, condition2)
    field.print9x9()





