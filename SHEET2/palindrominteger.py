n=int(input ("enter a number : "))
i=1
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum *10+r
    n=n//10
print("reverse of number is :" ,sum)
    
if(temp==sum):
    print("its a palindrome")
else:
    print("its not a palindrome")