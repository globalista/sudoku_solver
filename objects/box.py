class Box:
    def __init__(self, possible_values):
        # self.possible_values = possible_values
        self.possible_values = list(possible_values)
        self.value = None

    def make_copy(self):
        new_box = Box(list(self.possible_values))
        new_box.value = self.value
        return new_box

    def set_value(self, value):  # set value, poss_value=[]
        if value not in self.possible_values:
            raise ValueError('Nelze zapsat hodnotu')
        self.value = value
        self.possible_values = []

    def remove_from_possible_values(self, value):
        if value in self.possible_values:
            self.possible_values.remove(value)
            return True
        return False


