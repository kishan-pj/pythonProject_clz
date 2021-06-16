#required arguments
def sum(a,b):
    return a+b

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print(sum(a,b))

#defaulf arguments
def sum(a,b=2):
    return a+b

d=int(input("enter the first number: "))
e=int(input("enter the second number: "))
print(sum(a,b))

#keywoard arguments
def show(name,country):
    return name+" "+country

print(show(country="nepal",name="shyam"))

#arbitary argument
def sum(*nabin):
    sum=0
    for i in nabin:
        sum=sum+1
    print(nabin)

sum(1,2)
sum(2,3,4,5,6,7)



#Keyword arbitary arguments
def sum(**line):
    print(line)
    sum=0
    for i in line:
        sum=sum+i
    return sum

print(sum(a=2,b=3,c=4,d=10))



def sum():
    print(a,b)

a=10
b=5
sum()











