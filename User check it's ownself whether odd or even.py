# User check it's ownself whether odd or even

# take input from user

num = int(input("Give me a number to check : "))
check = int(input("Give me a number to divid by : "))


# Use if else statement

if num % 4 == 0:
    print(num, "is a multiple of 4")

elif num % 2 == 0:
    print(num, "is an even number ")

else:
    print(num, "is an odd number ")



# Another if...else statement to divid num on check 

if num % check == 0:
    print(num, "divides evenly by", check )

else:
    print(num,"does not divides evenly by", check)