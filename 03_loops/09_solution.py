## 9. List Uniqueness Checker

# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

# NOTE: set stores only unique elements in it..

unique_set = set()

for i in items:
    if i not in unique_set:
        print("duplicate : ",i)
        break
    unique_set.add(i)