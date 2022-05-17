year = int(input("Enter the year you want to checK :"))
leap = True

if year %4 == 0:
    if year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False
else:
    leap = False

if leap == True:
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")