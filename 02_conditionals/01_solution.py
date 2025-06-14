# age group categorization
# Classify the person's age group : child( < 13) , teenager(13-19) , adult(20-59) , senior(60+)
user_age = int(input("What is your age : "))
if user_age < 13:
    print("you are a CHILD")
elif user_age < 20:
    print("you are a TEENAGER")
elif user_age < 60:
    print("you are an ADULT")
else:
    print("you are a SENIOR")