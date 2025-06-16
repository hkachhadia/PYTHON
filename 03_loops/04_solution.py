## 4. Reverse a String

## Problem: Reverse a string using a loop.

s = str(input("Enter the string : "))
# print(x)
# print(s[::-1])
for x in range(len(s),0,-1):
    print(s[x-1], end = '')