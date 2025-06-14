## 10. Pet Food Recommendation

##Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
breed = str(input("Enter the type of an animal(dog or cat): ")).strip()
##strip removes the extra spaces before and after the string.
age = int(input("Enter the age of the animal: "))
if breed == "dog":
    if age <=0:
        print("check the age!!!")
        exit()
    if age < 2:
        print("puppy food")
    else:
        print("pedigree")
elif breed == "cat":
    if age <=0:
        print("check the age!!!")
        exit()
    if age>5:
        print("senior cat food")
    else:
        print("milk")