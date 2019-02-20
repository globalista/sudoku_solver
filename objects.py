class Box:
    def __init__(self):
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = None

    def set_value(self, value): #nastavi value, poss_value=[]
        if value in self.possible_values:
            self.value = value
            self.possible_values = []
            return True
        return False

    def remove_from_possible_values(self, value):
        if value in self.possible_values:
            self.possible_values.remove(value)
            return True
        return False


class Field:
    def __init__(self, matrix):
        self.field = []
        for i in range(m):
            new_line = []
            for j in range(n):
                new_box = Box()
                new_line.append(new_box)
            self.field.append(new_line)

    def print9x9(self):
        for i in range(9):
            for j in range(9):
                value = self.field[i][j].value
                if value:
                    print(value, end =' ' )
                else:
                    print('x', end = ' ')
                if j in {2, 5}:
                    print(' ', end = ' ')
                if j == 8:
                    print()
            if i in {2, 5}:
                print()



class Area:
    def __init__(self, list_of_coords, field):
        self.field = []
        self.nums_to_fill = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def remove_from_possible_values(self, value):
        if value in self.nums_to_fill:
            for box in self.field:
                box.remove_from_possible_values(value)
            self.nums_to_fill.remove(value)



if __name__ == '__main__':
    fieldtest = Field()
    fieldtest.load_input('vstup')
    fieldtest.print9x9()







