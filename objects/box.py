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


