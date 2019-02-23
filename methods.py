def input_to_matrix(vstup):
    matrix = []
    with open(vstup) as f:
        for line in f:
            line1 = line.strip().split()
            if line1:
                final_line = []
                for j in line1:
                    if j in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                        final_line.append(int(j))
                    else:
                        final_line.append(0)
                matrix.append(final_line)
    return matrix

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


def load_input(field, matrix, areas):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                set_value_and_delete_it_from_areas(field.field[i*9+j], areas, matrix[i][j])
