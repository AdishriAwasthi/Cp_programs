a = int(input("Enter a number: "))
i = 1
t = 0

while i <= a:
    if i % 2 == 0:  
        t += i      
    i += 1           

print("The sum of all even numbers is:", t)