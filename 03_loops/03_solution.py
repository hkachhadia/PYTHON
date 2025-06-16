## 3. Multiplication Table Printer

## Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
n = int(input("Enter the number: "))
t= 0
for t in range(11):
    if t == 5:
        continue
    print(str(n) + " x " + str(t) + " = " + str(n * t))