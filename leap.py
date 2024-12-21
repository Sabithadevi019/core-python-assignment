def leap_year(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    else:
        return False
n=int(input("Enter a year:"))
if leap_year(n):
    print(n,"is Leap Year")
else:
    print(n,"not a Leap Year")