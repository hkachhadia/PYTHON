# Grade Calculator
# Assign a letter grade based on a student's score: A(90-100),B(80-89),C(70-79),D(60-69),F(below 60)
marks = int(input("Enter your marks: "))
if marks > 100:
    print("please check the marks!!")
    exit()

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(marks,"marks = ",grade," grade.")