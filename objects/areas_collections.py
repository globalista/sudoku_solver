class AllAreas:
    def __init__(self):
        self.list_of_all_areas = []

    def add_area(self, area):
        self.list_of_all_areas.append(area)

    def areas_containing_the_box(self, box):
        areas_containing = []
        for area in self.list_of_all_areas:
            if box in area.field:
                areas_containing.append(area)
        return areas_containing

    def set_value_and_delete_it_from_areas(self, box, value):
        try:
            box.set_value(value)
        except ValueError:
            raise ValueError('z nejakeho duvodu nelze zapsat hodnotu', value, box.possible_values)
        for area in self.areas_containing_the_box(box):
            area.remove_from_possible_values(value)
