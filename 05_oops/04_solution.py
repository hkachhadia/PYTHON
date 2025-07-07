class car:
    __brand = "BMW"
    @staticmethod
    def getter():
        return car.__brand
    
# print(car1.__brand)
result  = car.getter()
print(result)