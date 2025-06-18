# 6 Lambda Function

# Problem: Create a lambda function to compute the cube of a number.

# def cube(num):
#     return num**3
# print(cube(4))
    
cube = lambda x: x**3
print(cube(9))

# Functions similar to lambda:
# - def: Standard function definition.
# - functools.partial: Creates a new function with some arguments fixed.
# - operator.methodcaller / operator.attrgetter: Returns callable objects.
# - types.FunctionType: Dynamically creates functions.
