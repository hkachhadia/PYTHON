## 9. Leap Year Checker

## Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter the year: "))
if(year % 4 == 0 or year % 400 == 0 and year % 100 !=0):
    print("Leap year")
else:
    print("not a Leap year")