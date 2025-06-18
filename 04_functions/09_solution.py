# 9 Generator Function with yield

# Problem: Write a generator function that yields even numbers up to a specified limit.
def generate_even(num):
    for i in range(2,num + 1,2):
        yield(i)
for i in generate_even(20):
    print(i)