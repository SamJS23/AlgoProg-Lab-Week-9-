#CLASS EXERCISE

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

    def paint_house(self, paint_house):
        print(f"Changing the color of the house to {paint_house}.")
        self.color = paint_house 

    def add_garage(self):
        if self.has_garage:
            print(f"The house already has a garage.")
        else:
            print(f"Adding a garage to the house.")
            self.has_garage = True

    def set_address(self, set_address):
        print(f"Changing the address of the house from {self.address} to {set_address}.")
        self.address = set_address



house1 = House(floors=3, doors=4, windows=7, color="Red", address="456 Side St")

house1.display_info()
print()

house1.paint_house("Green")

house1.add_garage()

house1.set_address("808 Sudirman St")

house1.display_info()
print()


House.display_total_houses()
print()