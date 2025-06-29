#First check divisible by 4
#Then check divisible by 100
#If yes, check divisible by 400 to confirm leap year

year = int(input("Enter the year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")