n=list(map(int,input().split()))
for i in range(len(n)):
    n.sort()
print("min" ,n[0],"max",n[-1])