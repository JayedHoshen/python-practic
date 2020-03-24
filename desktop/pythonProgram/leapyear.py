year = input("Please enter any year:")
year = int(year)

if year % 100 !=0 and year % 4 == 0:
    print(year,"is Leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print(year,"is Leap year.")
else:
    print(year,"is not any leap year.")

print("Done!")
