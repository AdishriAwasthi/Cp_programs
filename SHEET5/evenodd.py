
n=list(map(int,input().split()))
s=0
p=0
for i in range (len(n)):
    if n[i]%2==0:
        s+=1
    else:
        p+=1

if s > p:
    print(s - p)
else:
    print(p - s)

#OUTPUT
# 1 2 3 4 5
# 1
