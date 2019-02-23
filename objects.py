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
    def __init__(self, m=9, n=9):
        self.field = []
        for i in range(m*n):
            new_box = Box()
            self.field.append(new_box)


    def print9x9(self):
        for i in range(9):
            for j in range(9):
                value = self.field[i*9 + j].value
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
        print()


class Area:
    def __init__(self, list_of_coords, field):
        self.field = []
        for i,j in list_of_coords:
            self.field.append(field.field[i*9+j])
        self.nums_to_fill = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def remove_from_possible_values(self, value):
        if value in self.nums_to_fill:
            for box in self.field:
                box.remove_from_possible_values(value)
            self.nums_to_fill.remove(value)



if __name__ == '__main__':
    fieldtest = Field()

    fieldtest.print9x9()







