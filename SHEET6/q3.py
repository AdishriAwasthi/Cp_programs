# WriteaprogramtoinputTstrings(S)fromuserandprint1ifitispalindromeotherwiseprint0.
#  NOTE:Astringispalindromeifitreadsthesamefrombackwardasfromforward.
#  Input:
#  3
#  abcba
#  axax
#  abba
#  Output:
#  1
#  0
# #  1


n = int (input())
for i in range(n):
    s=input()
    if s==s[::-1]:
        print("1")
    else:
        print("0")