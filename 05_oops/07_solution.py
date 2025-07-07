class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def general_description():
        return "A car is a vehicle with four wheels, used for transporting people."

# Example usage:
# print(Car.general_description())
# a static method can be directly call by the CLASS itself without any OBJECT of that class...