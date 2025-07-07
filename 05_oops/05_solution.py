class car:
    brand = "BMW"
    model = "M4"


    def fuel_type():
        type_1 = "petrol"
        type_2 = "diesel"
        return type_1,type_2 
class Electric_Car(car):
    battery_size = "50kw"


    def fuel_type():
        type_1 = "electricity"
        return type_1


car1 = car.fuel_type()

car2 = Electric_Car.fuel_type()

print(car1)
print(car2)