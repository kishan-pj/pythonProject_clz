# function having no paremeter and no return type.

def sum():
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: " ))
    print(f"the sum of {a } and {b} is {a+b}")

sum()


# function having peremeter and with no return type.

def sum(a,b):
    print(f"the sum of {a} and {b} is {a+b}")

sum(4,5)

# function having paremeter and return type .

def sum(x,y):
    return x+y

a=int(input("enter first number"))
b=int(input("enter the second number"))
c=sum(2,3)
print(c)