# ● 
# Below 25 – D 
# ● 
# 25 to 45 – C 
# ● 
# 45 to 65 – B 
# ● 
# 65 to 85 – A 
# ● 
# Above 85 – A+ 
n=int(input("enter your marks \n"))
if n >=85:
    print("A+")
elif n <85 and n>=65:
    print("A")
elif n <65 and n>=45:
    print("B")
elif n <45 and n>=25:
    print("C")
elif n <25:
    print("D")
else:
    print("invalid")