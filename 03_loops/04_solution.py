## 4. Reverse a String

## Problem: Reverse a string using a loop.

s = str(input("Enter the string : "))
rev_str = ""

# solution 0(WITHOUT LOOP)
# print(s[::-1])

# solution 1
# for x in range(len(s),0,-1):
#     print(s[x-1], end = '')

# solution 2
for char in s:
    rev_str = char + rev_str
print(rev_str)