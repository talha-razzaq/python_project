# Even Odd game

#take user input
num = float(input("Enter the number : "))
print("your entered number num", num)

if num == 0:
    print("'Please enter valid number' is ", num)

elif (num % 2) == 0:
    print("'Even number' is", num)

else:
    print("'Odd number' is ", num)
