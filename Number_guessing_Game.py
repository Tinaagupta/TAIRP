import random
number=random.randrange(1,101)
print("The Number to be choosen is below 101")
userInput=int(input("Enter Your Number : "))
if userInput>number:
    print("Computer Number", number)
    print("Your guess number is too high")
elif userInput<number:
    print("Computer Number", number)
    print("Your guess number is too low")
else:
    print("Computer Number", number)
    print("Your guess number is equal")
