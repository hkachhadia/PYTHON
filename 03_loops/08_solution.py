## 8. Prime Number Checker

# Problem: Check if a number is prime.
num = int(input("Enter the number : "))
for i in range(2,num):
    if num%i==0:
        print("NOT prime")
        break
    else:
        print("prime")
        break