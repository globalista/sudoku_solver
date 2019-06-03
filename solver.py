from copy import deepcopy


def solver(task):
    still_working = True
    while still_working:
        still_working = False
        for condition in task.conditions:
            try:
                if condition(task):
                    still_working = True
            except ValueError:
                return
    return task


def solver_with_recursion(task):
    if task.field.solved():
        return task
    values_to_try = task.field.find_the_first_unsolved_box().possible_values
    print(values_to_try)
    for value in values_to_try:
        new_task = deepcopy(task)
        the_box = new_task.field.find_the_first_unsolved_box()
        print(value, new_task.field.field.index(the_box))
        new_task.areas_collection.set_value_and_delete_it_from_areas(the_box, value)
        new_result = solver(new_task)
        if new_result:
            return solver_with_recursion(new_result)