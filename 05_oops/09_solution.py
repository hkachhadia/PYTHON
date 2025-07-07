class car:
    def __init__(self,brand,model,fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel
class electric_car(car):
    def __init__(self,brand, model,fuel):
        super().__init__(brand,model,fuel)
        # self.brand = brand
        # self.model = model

carX = electric_car("TESLA","X","energy")
print(isinstance(carX,electric_car)) #TRUE
print(isinstance(carX,car)) #TRUE