def solver(field, areas, condition1,  condition2, symbols_to_fill):
    still_working = True
    n=0
    while still_working:
        print(n)
        n+=1
        still_working = False
        if condition1(field, areas):
            still_working = True
        if condition2(areas, symbols_to_fill):
            still_working = True
