#  Print 1 if all the characters of the character array are alphabetical (a-z and A-Z), else print 0.
#  Input:
#  A=Python
#  Output:
#  1
s=input()
f=1
for i in s :
    if not i.isalpha():
        f=0
        break
print(f)