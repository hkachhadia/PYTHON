## 8. Password Strength Checker

##Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)
password = str(input("Enter your password: "))
if len(password) <= 0 or len(password) > 16:
    print("check your password!!!")
    exit()
if len(password) > 10:
    print("strong password!!")
elif len(password) > 6:
    print("medium password!!")
elif len(password) <= 6:
    print("weak password!!")
