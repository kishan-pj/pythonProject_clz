def mul_tab(num):
    for i in range(1,11):
        pro=num*i
        print(f"{num}*{i}={pro}")

num=int(input("enter number for multiplication: "))
mul_tab(num)