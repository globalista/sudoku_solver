def solver(task):
    still_working = True
    did_something = False
    while still_working:
        still_working = False
        for condition in task.conditions:
            if condition(task):
                still_working = True
                did_something = True
    return did_something
