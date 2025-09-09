n = int(input("enter a number : "))
for i in range (n,0,-1):

    for j in range ( 2*i-1):
            print("*",end=" ")
    print()

# output
# * * * * * * * * * 
# * * * * * * *
# * * * * *
# * * *
# *