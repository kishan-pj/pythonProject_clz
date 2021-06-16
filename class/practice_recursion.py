import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=0
def greet():
    global i
    i+=1
    print("hello",1)
    greet()

greet()


def fac(n):
    if(n==0):
        return 1
    return n*fac(n-1)

result=fac(5)
print(result)