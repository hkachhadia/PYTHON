# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance = int(input("Enter the distance(in km): "))
if distance < 0:
    print("check your value!!!") 
    exit()
if distance >= 15:
    print("use car")
elif distance < 15 and distance > 3:
    print("use bike")
elif distance <=3:
    print("walk")