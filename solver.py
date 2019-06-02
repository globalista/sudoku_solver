def solver(task):
    still_working = True
    while still_working:
        still_working = False
        for condition in task.conditions:
            if condition(task):
                still_working = True
    return task
