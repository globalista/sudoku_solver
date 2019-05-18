from . import box


class Field:
    def __init__(self, length, possible_values):
        self.field = []
        for i in range(length):
            new_box = box.Box(possible_values)
            self.field.append(new_box)

    def solved(self):
        return all(i.value for i in self.field)

    def print_in_n_columns(self, n):
        for i in self.field:
            if i.value:
                print(i.value, end=' ')
            else:
                print('x', end=' ')
            if self.field.index(i) % n == n-1:
                print()

    def print9x9(self):
        for i in range(9):
            for j in range(9):
                value = self.field[i*9 + j].value
                if value:
                    print(value, end=' ')
                else:
                    print('x', end=' ')
                if j in {2, 5}:
                    print(' ', end=' ')
                if j == 8:
                    print()
            if i in {2, 5}:
                print()
        print()
        print()

    def find_the_first_unsolved_box(self):
        for i in self.field:
            if not i.value:
                return i
