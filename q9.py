#  Write a program to reverse the words present in a string. Check example input/output.
#  Input:
#  Everyone loves data science
#  Output:
#  enoyrevE sevol atad ecneics
s=input()
w=s.split()
r=" " 
for i in w:
     m= i[::-1]
     r+=m +" "
print(r)
