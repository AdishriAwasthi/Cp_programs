# You are given a character string A, having length N and an integer ASCII code B.
#  You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or
#  report that it does not exist.
#  Input:
#  A="aabbcc"
#  B=98
#  Output:
#  2
s=input()
b=int(input())
for i in range(len(s)):
    if ord(s[i])==b:
        print(i)
        break
else:
    print(-1)
