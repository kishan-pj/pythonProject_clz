def fac(num):
 product=1
 for i in range(2, num + 1):
    product = product * i
 return product

num=int(input("enter a number for factorial: "))
fac(num)


