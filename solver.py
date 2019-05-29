def solver(task, condition1, condition2):  #(field, all_areas, condition1,  condition2, symbols_to_fill):
    still_working = True
    did_something = False
    while still_working:
        still_working = False
        if condition1(task):  # (field, all_areas):
            still_working = True
            did_something = True
        if condition2(task):  # (all_areas, symbols_to_fill):
            still_working = True
            did_something = True
    return did_something
