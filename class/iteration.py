for i in range(1,10,1):
    if i%2==0:
        print(i,":even")
    else:
        print(i,":odd")


for val in "string":
    if val == "i":
        continue
    print(val)
else:
     print("end")

fruits=["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
else:
    print("end")

num=5
product=1
for i in range (1,num+1):
    product=product*i
print(f"the factorial of {num} is {product}")



a=40
b=40
if b>=a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
