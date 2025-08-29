n =int(input("enter a year :\n"))
if (n %4==0 )and(  n % 100 !=0 or n % 400==0):
    print("its a leap year")
else:
    print("not a leap year")
    