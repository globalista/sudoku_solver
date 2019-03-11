class Box:
    def __init__(self, possible_values):
        self.possible_values = possible_values
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


