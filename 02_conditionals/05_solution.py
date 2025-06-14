# Weather Activity Suggestion
# suggest an activity based on the weather(eg: sunny = go for a walk,rainy = read a book,snowy = build a snowman)
weather = str(input("Enter the weather: "))
if weather == "sunny":
    status = "go for a walk"
elif weather == "rainy":
    status = "read a book"
elif weather == "snowy":
    status = "build a snowman"
else:
    print("check the weather!!")
    exit()
print(status)

