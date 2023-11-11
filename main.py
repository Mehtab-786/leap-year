# characteristics of Leap  year


# every year that is divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also divisible by 400


year = int(input("enter the year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is  not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is  not a leap year")

