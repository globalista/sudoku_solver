def solver(field, all_areas, condition1,  condition2, symbols_to_fill):
    still_working = True
    n=0
    while still_working:
        print(n)
        n+=1
        still_working = False
        if condition1(field, all_areas):
            print("c1")
            still_working = True
        if condition2(all_areas, symbols_to_fill):
            print("c2")
            still_working = True
