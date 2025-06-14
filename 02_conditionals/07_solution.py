## 7. Coffee Customization

##Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
size = str(input("Enter the size of the coffee: "))
extra_shot = bool(int(input("if you need an extra espresso shot (1/0): ")))
if extra_shot:
    print(size + " with extra shot")
else:
    print(size + " without extra shot")
