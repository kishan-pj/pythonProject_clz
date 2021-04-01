# write a program to find am or pm from the time given by user.

time=int(input("enter the number:"))
if time<=12:
    print("enter the time is am")
elif time>=12:
    print("enter the time is pm")
print("the program is over")