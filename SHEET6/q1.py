# WriteaprogramtoinputTstrings(S)fromuserandprintcountofvowelsandconsonantsinit.
#  Input:
#  2
#  List
#  Apple
#  Output:
#  13
#  23


n = int(input())

for i in range(n):
    s = input()
    v = 0
    c = 0
    for ch in s:
        if ch in 'aieouAIEOU':
            v += 1
        else:
            c += 1
    print(v, c)

