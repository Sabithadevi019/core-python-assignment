def prime(n):
    if n==2:
        print("It is a prime number")
    elif n>2:
        for i in range(2,n):
            if n%i==0:
                return False
            return True
n=int(input("Enter a number:"))
if prime(n):
    print(n,"It is a prime number")
else:
    print(n,"is not a prime number")