# Task 1 The Greatest Showdown

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter your final number: "))

if number1 and number2 < number3:
    print("This is the greatest number " + str(number3))
elif number2 and number3 < number1:
    print("This is the greatest number " + str(number1))
else:
    print("This is the greatest number " + str(number2))

# Task 2

if number1 and number2 > number3:
    print("This is the smallest number " + str(number3))
elif number2 and number3 > number1:
    print("This is the smallest number " + str(number1))
else:
    print("This is the greatest number " + str(number2))