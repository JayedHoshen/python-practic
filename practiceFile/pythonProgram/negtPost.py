number = input("Please enter any interger number:")
number = int(number)

if number > 0:
    print(number,"is a Positive number.")
elif number < 0:
    print(number,"is a Negative number. ")
elif number == 0:
    print(number,"is Zero")
else:
    print(number,"is not a number!")
print("Done!")
