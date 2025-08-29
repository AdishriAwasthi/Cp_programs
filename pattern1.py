# n=(int(input("enter a number :")))
# for i in range (1 , n+1):
#     print("*",end=" ")

#    GRID PATTERN

# n =int(input("enter a number columns : "))
# m =int(input("enter a number rows : "))
# for i in range (1,n+1):
#     for j in range(1,m+1):
#         print("*",end ="  ")
#     print()


# n =int(input("enter a number  : "))

# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print("*",end ="  ")
#     print()


# OUTPUT
    
# *  
# *  *
# *  *  *
# *  *  *  *

# # n =int(input("enter a number  : "))

# # for i in range (n,0,-1):
# #     for j in range(i):
# #         print("*",end ="  ")
#     print()

# OUTPUT

# *  *  *  *  
# *  *  *
# *  *
# *

# n =int(input("enter a number  : "))

# for i in range (1,n+1):
#     for j in range(1,i+1):
#      if(j%2==0):
#         print("*", end=" ")
#      else:
#         print(j, end =" ")
#     print()

# OUTPUT
    
# 1 
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5

# n =int(input("enter a number  : "))

# for i in range (1,n+1):
#     for j in range(1,n+1):
#      if(j==1 or j==n):
#         print("*", end=" ")
#      else:
#         print("-", end =" ")
#     print()
    

# OUTPUT

# * - - - * 
# * - - - *
# * - - - *
# * - - - *
# * - - - *

# n =int(input("enter a number  : "))

# for i in range (n,0,-1):
#     for j in range(1,i+1):
#      if(j==1 or j==i):
#         print("*", end=" ")
#      else:
#         print("-", end =" ")
#     print()

# *---*
# *--*
# *-*
# # *
# n = int (input("enter a number"))
# for i in range (n,0,-1):
#   print("-",end=" ")
# for j in range(1,n+1):
#      if(j==1 or j==n):
#         print("*", end=" ")
#      else:

# ----*
# ---**
# --***
# -****
# ***** 

# upper ka opp bhe krna hai 

n=int(input("enter a number "))
for i in range (1,n+1):
   for j in range(n-i+1):
      print("*",end=" ")
   for j in range (2*i-2):
      print(" ", end =" ")
   for j in range (n-i+1):
      print("*",end=" ")
   print()

# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 

# n=int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    
    print()


# * * * * * * * * * * 
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *