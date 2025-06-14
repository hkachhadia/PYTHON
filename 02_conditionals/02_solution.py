# Movie Ticket Pricing 
# Movie Tickets  are priced based on age: $12 for adults(18 and over),$8 for childern. EVERYONE GETS A $2 DISCOUNT ON WEDNESDAY.

    # SOLUTION - 1
# age  = int(input("Enter your age: "))
# day = str(input("Enter the day: "))
# if day == "wednesday":
#     if age < 18:
#         print("you are a child and today is wednesday therefore ticket price is $6")
#     elif age >= 18:
#         print("you are an adult and today is wednesday therefore ticket price is $10")
# else:
#     if age < 18:
#         print("you are a child and today is not wednesday therefore ticket price is $8")
#     elif age >= 18:
#         print("you are an adult and today is not wednesday therefore ticket price is $12")
    

    # SOLUTION - 2
age  = int(input("Enter your age: "))
day = str(input("Enter the day: "))
price = 12 if age >= 18 else 8 #new syntax
if day == "wednesday":
    price-=2
print(price)