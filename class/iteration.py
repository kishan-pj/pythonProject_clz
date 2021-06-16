
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



a=40
b=40
if b>=a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
