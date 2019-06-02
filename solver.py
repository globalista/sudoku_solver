def solver(task, conditions):
    still_working = True
    did_something = False
    while still_working:
        still_working = False
        for condition in conditions:
            if condition(task):
                still_working = True
                did_something = True
    return did_something
