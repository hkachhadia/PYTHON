# create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    def __init__(self,battery_size):
        self.battery_size = battery_size
class Engine:
    def __init__(self,engine_size):
        self.engine_size = engine_size
class ElectricCar(Battery, Engine):
    def __init__(self, brand, battery_size, engine_size):
        Battery.__init__(self, battery_size)
        Engine.__init__(self, engine_size)
        self.brand = brand

carX = ElectricCar("TESLA", "100KW", "NO ENGINE")
print(vars(carX)) #vars - it is used to display all the attributes of the class in the dictionary form
        