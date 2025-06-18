# 10 Recursive Function

# Problem: Create a recursive function to calculate the factorial of a number.
def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)

n = int(input("Enter the number: "))
print("factorial : ",factorial(n))