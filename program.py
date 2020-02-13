from process_input import initialize
from solver import solver, solver_with_recursion
from conditions import conditions


list_of_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#input_values = 'zadani_soubory/pp1836'
#input_areas =  'zadani_soubory/klasik_9x9'
input_values = 'zadani_soubory/logika19_4/10_parkety'
input_areas = 'zadani_soubory/logika19_4/10_pole'

field_length = 81


if __name__ == '__main__':
    task = initialize(list_of_values, input_values, input_areas, field_length, conditions)
    result = solver(task)
    print(result.field.solved())
    result.field.print9x9()
    print()
    result = solver_with_recursion(result)
    result.field.print9x9()




