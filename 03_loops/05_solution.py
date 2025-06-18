## 5. Find the First Non-Repeated Character

# Problem: Given a string, find the first non-repeated character.

s = str(input("Enter the string: "))
# kachhadia -> k
# hhappy -> a
for i in s:
    if s.count(i) == 1:
        print(i)
        break

