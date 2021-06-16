def factotial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factotial(num-1)
print(factotial(5))

def multiplication(num):
    if num==1:
        return 3
    else:
        return 3+multiplication(num-1)
for i in range(1,11):
    print(multiplication(i))

l=[2,4,6,8]
def suml(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+sum(l[1:])
print(sum(l))






