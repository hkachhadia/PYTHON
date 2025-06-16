## 2. Sum of Even Numbers

## Problem: Calculate the sum of even numbers up to a given number n.
n = int(input("Enter the number : "))
sum = 0
for x in range(n):
    if x%2==0:
        sum = sum + x
print(sum)
