year=int(input("Enter a year: "))

if year % 4 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} a leap year")
else:
    print(f"{year} is not a leap year")