# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
import time
def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def example(a,b):
    time.sleep(5)
    return (a+b)

print(example(3,4))
print(example(3,4))
print(example(4,3))
print(example(4,4))