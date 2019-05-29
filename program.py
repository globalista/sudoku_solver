from process_input import initialize
from conditions import condition1, condition2
from solver import solver


list_of_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
input_values = 'zadani_soubory/pp1836'
input_areas = 'zadani_soubory/klasik_9x9'
field_length = 81

if __name__ == '__main__':
    task = initialize(list_of_values, input_values, input_areas, field_length)
    solver(task, condition1, condition2)
    print(task.field.solved())
    task.field.print9x9()
