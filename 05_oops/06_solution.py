# Problem: Add a class variable to Car that keeps track of the number of cars created.
class car:
    brand = "BMW"
    model = "M4"
    count = 0  # Class variable to keep track of the number of cars created 
    def __init__(self):
        car.count += 1  # Increment the count each time a new car is created    

class Electric_Car(car):
    battery_size = "50kw"               

car1 = Electric_Car()
car2 = Electric_Car()       
car3 = Electric_Car()
print("Number of cars created:", car.count)  # Output the count of cars created
print(car1.brand)
print(car1.model)
print(car1.battery_size)
print(car2.brand)       
print(car2.model)
print(car2.battery_size)
print(car3.brand)   
print(car3.model)
print(car3.battery_size)

