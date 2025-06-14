#Fruit Ripeness Checker 
# Determine if a fruit is ripe,overripe or unripe based on its color.(eg: Banana : green = unripe, yellow = ripe, brown = overripe).
color = str(input("Enter the color of Banana : "))
if color == "green":
    status = "UNRIPE"
elif color == "yellow":
    status = "RIPE"
elif color == "brown":
    status = "OVERRIPE"
else:
    print("verify the color!!")
    exit()
print(status)