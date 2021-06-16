# no paremeter and no return type
def sum():
    a=6
    b=7
    print(f"sum of {a} and {b}is {a+b}")

sum()

def mul():
    a=2
    b=3
    print(f" mul of {a} and {b} is {a*b} ")

mul()

def sub():
    a=3
    b=2
    print(f"sub of {a} and {b} is {a-b}")

sub()

def division():
    a=4
    b=2
    print(f"division of {a} and {b} is {a/b} ")

division()


# parameter and no return type
def add(a,b):
    print(f"sum of {a} and {b} is {a+b}")

add(2,2)


def sub(a,b):
    print(f"sub of {a} and {b} is {a-b}")

sub(4,2)

def mul(a,b):
    print(f"mul of {a} and {b} is {a*b}")

mul(2,2)

def division(a,b):
    print(f"division of {a} and {b} is {a/b} ")

division(4,2)


# parameter and return type
def add(a,b):
    return a+b

a=int(input("enter the fir_num: "))
b=int(input("enter the sec_num: "))
c=add(2,4)
print(c)

def sub(a,b):
    return a-b

a=int(input("enter fir_num: "))
b=int(input("enter sec_num: "))
c=sub(4,2)
print(c)

def mul(x,y):
    return x*y

x=int(input("enter the fir_num: "))
y=int(input("enter sec_num: "))
c=mul(2,2)
print(c)

# no parameter and return type
def add():
    a=int(input("enter fir_num: "))
    b=int(input("enter sec_num: "))
    return a+b

c=add()
print()

# multiplication table
num=2
for i in range(1,11):
    prod=num*i
    print(f"{num}*{i}={prod}")

def prod():
    num = 2
    for i in range(1, 11):
        prod = num * i
        print(f"{num}*{i}={prod}")

prod()

def prod(num,i):
    return num*i


num = 2
for i in range(1, 11):
    prod = num * i
    print(f"{num}*{i}={prod}")


def call():
    return

a=0
for i in range(4):
    for j in range(4-i):
        print(a,end=" ")
        a=a+1
    print()


