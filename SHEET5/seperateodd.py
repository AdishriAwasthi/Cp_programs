n=list(map(int,input().split()))
s=0
m=0
for i in range(len(n)):
    if n[i]%2==0:
        s+=1
        print(n[i])
    else:
        m+=1
        print(n[i])
# print(s)
# print(m)