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
        print(len(areas_containing), len(areas_containing[2].field))
        return areas_containing

    def set_value_and_delete_it_from_areas(self, box, value):
        if box.set_value(value):
            for area in self.areas_containing_the_box(box):
                area.remove_from_possible_values(value)
        else:
            raise ValueError('z nejakeho duvodu nelze zapsat hodnotu', value, box.possible_values)
