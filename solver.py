def solver(field, areas, condition1,  condition2):
    still_working = True
    while still_working:
        still_working = False
        if condition1(field, areas):
            still_working = True
        if condition2(areas):
            still_working = True
