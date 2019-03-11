class Area:
    def __init__(self, list_of_boxes, symbols_to_fill):
        self.field = list_of_boxes
        self.nums_to_fill = symbols_to_fill

    def remove_from_possible_values(self, value):
        if value in self.nums_to_fill:
            for box in self.field:
                box.remove_from_possible_values(value)
            self.nums_to_fill.remove(value)