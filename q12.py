#  Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, print 0.
#  Input:
#  A=Python45
#  Output:
#  1
s=input()
f=1
for i in s:
    if not i .isalnum():
        f=0
        break
print(f)