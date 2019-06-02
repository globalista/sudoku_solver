from . import field, areas_collections
from conditions import conditions


class Task:
    def __init__(self, length, symbols_to_fill):
        self.field = field.Field(length, symbols_to_fill)
        self.areas_collection = areas_collections.AllAreas()
        self.symbols = symbols_to_fill
        self.conditions = conditions
