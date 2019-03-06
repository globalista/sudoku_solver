from .box import Box

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
        print()
