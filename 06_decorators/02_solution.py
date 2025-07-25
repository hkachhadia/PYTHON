# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def print_func(func):
    def label(*arg):
        print("function name : ",func.__name__)
        print("argument : ",*arg)
    return label

@print_func
def example(*arg):
    print("example started!!")

example(4,3,4,3,4,4,5)







# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.
#         items())
#         print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return func(*args, **kwargs)
    
#     return wrapper

# @debug
# def hello():
#     print("hello")

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")

# hello()
# greet("chai", greeting="hanji ")