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