def solver(field, all_areas, condition1,  condition2, symbols_to_fill):
    still_working = True
    while still_working:
        still_working = False
        if condition1(field, all_areas):
            still_working = True
        if condition2(all_areas, symbols_to_fill):
            still_working = True
