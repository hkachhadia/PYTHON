# 4 Function Returning Multiple Values

# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def circle(r):
     area = math.pi * r ** 2
     circum = 2 * math.pi * r
     return area,circum
a,c = circle(2)
print("area : ",a)
print("circumference : ",c)
