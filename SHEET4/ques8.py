n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i == (n // 2) + 1:   
        print("*")
    else:
        print("* *")
    
# output
# * *
# * *
# *
# * *
# * *