n=int(input("enter a number : "))
i=1
while i <=n:
    if i%2!=0:
     i+=1
     continue
    
    print(i , end =" ")
    i+=1