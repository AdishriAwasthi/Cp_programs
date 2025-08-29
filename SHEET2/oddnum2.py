a = int(input("enter a number : "))
i =1
sum=0

while i <=a:
    if  i % 2!=0:
        sum+=i
    i+=1

print(" sum of odd numbers from 1 and", a, "are:", sum)
