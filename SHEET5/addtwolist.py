n=list(map(int,input().split()))
m=list(map(int,input().split()))
r=[]
for i in range (min(len(n),len(m))):
    r.append(n[i]+m[i])
print(r)
    