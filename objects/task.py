from . import field, areas_collections


class Task:
    def __init__(self, length=0, symbols=[]):
        self.field = field.Field(length, symbols)
        self.areas_collection = areas_collections.AllAreas()
        self.symbols = symbols
