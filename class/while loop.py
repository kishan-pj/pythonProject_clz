
import random

number=random.randint(1,10)
guess=int(input("please guess the number"))
while number !=guess:
    guess=int(input("Uffs !! try again : guess again"))
else:
    print("congraluation!!! U r right")