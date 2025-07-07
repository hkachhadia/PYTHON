class Car:
    def __init__(self,brand,model):
        self.__brand = brand #private
        self.__model = model
    @property
    def model(self):
        return self.__model


my_car = Car(brand = "kia",model = "seltos")
# print(my_car.brand) private
# my_car.model = "kylaq"#cannot be overwrite due to the @property decorator

# print(my_car.model())  ---> print(my_car.model)
print(my_car.model)
        