# check through divisor

__author__ = "TALHA RAZZAQ"

print(__author__)

num = int(input("Enter the number : "))
print("You chose the number : ", num)  

dividedrange = list(range(1, num + 1))

dividedlist = []

for number in dividedrange:
    if num % number == 0:
        dividedlist.append(number )

print(dividedlist)