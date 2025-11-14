#  You are given a character string A. You to trim leading asterisk characters('*') in the string and
#  print the resultant string.
#  Input:
#  A="**h*e*l*lo*"
#  Output:
#  h*e*l*lo*
s=input()
m=s.lstrip("*")
print( m)