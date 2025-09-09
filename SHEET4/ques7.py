n = int(input("enter a number : "))
for i in range(1,n+1):
    print("*", end= " ")
print()
for j in range(n -2):
    print("* *")
for j in range(1, n+1):
    print("*",end =" ")


# output
# * * * * * 
# * *
# * *
# * *
# * * * * *
