# 7 Function with *args

# Problem: Write a function that takes variable number of arguments and returns their sum.
def sum_all(*args):
    print(args) #formatting (tuple)
    for i in args:
        print(i*2) # number  multiply by 2
    return sum(args) # sum of all the numbers

print("sum : ",sum_all(1,2,3,4,5,6,7,8,9,10))