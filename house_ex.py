class House:
    """A simple house class"""

    total_house = 0  # Keep track of the total number of houses

    def __init__(self, floors, doors, windows, color="White", has_garage=False, address=""):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address

        # Increment
        House.total_house += 1

    def display_info(self):
        """Displays attribute information of a house object."""
        print("House Information: ")
        print(f"    - Address: {self.address}")
        print(f"    - Doors: {self.doors}")
        print(f"    - Floors: {self.floors}")
        print(f"    - Windows: {self.windows}")
        print(f"    - Color: {self.color}")
        print(f"    - Has Garage: {'Yes' if self.has_garage else 'No'}")

    @classmethod
    def display_total_houses(cls):
        print(f"Total number of houses = {cls.total_house}")

    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False    # Not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False    # Floors, Doors, Windows should all be positive integers

        return True

    def paint_house(self, change_color):
        print(f"Painting the house at {self.address} to {change_color}.")
        self.color = change_color

    def add_garage(self):
        if self.has_garage:
            print(f"The house at already has a garage.")
        else:
            print(f"Adding a garage to the house at {self.address}.")
            self.has_garage = True

    def set_address(self, new_address):
        print(f"Changing the address of the house from {self.address} to {new_address}.")
        self.address = new_address



# Creating instances (objects) of the House class
house1 = House(floors=2, doors=3, windows=6, color="Blue", has_garage=True, address="123 Main St")
house2 = House(floors=1, doors=2, windows=4, address="123 Main St")

house1.display_info()
print()
house2.display_info()
print()
House.display_total_houses()
print()

validation_result = House.validate_house(house2)
print(f"House Validation Result: {'Valid' if validation_result else 'Invalid'}")

