from process_input import initialize
from conditions import condition1, condition2
from solver import solver

if __name__ == '__main__':
    field, all_areas = initialize(['1', '2', '3', '4', '5', '6', '7', '8', '9'],'zadani_soubory\\vstup','zadani_soubory\\klasik_9x9')
    solver(field, all_areas, condition1, condition2, ['1', '2', '3', '4', '5', '6', '7', '8', '9'] )
    field.print9x9()




