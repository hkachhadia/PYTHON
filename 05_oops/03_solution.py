class car:
    brand = "BMW"
    model = "M4"
class Electric_Car(car):
    battery_size = "50kw"

car1 = Electric_Car()
print(car1.brand)
print(car1.model)
print(car1.battery_size)
