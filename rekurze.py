from solver import solver
from conditions import condition1, condition2


def do_solving(the_field, all_areas, symbols):
    if the_field.solved():
        return the_field

    box = the_field.find_first_unsolved_box()
    position = the_field.field.index(box)
    for i in box.possible_values:
        new_field = the_field.make_copy()
        all_areas.set_vaue_and_delete_it_from_areas(new_field.field[position], i)
        solver(new_field, condition1, condition2, symbols)
        do_solving(new_field, all_areas, symbols)








