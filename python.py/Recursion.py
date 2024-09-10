# def show(n):
#     for i in range (5,0,-1):
#         print(i)
#     print(n)
        
# show(5)

# recursive function
"""def show(n):
   if(n==0):
      return
   print(n)
   show(n-1)
   
show(5)"""

# def fact(n):
#     if (n==0 or n == 1):
#         return 1
#     else:
#         return fact(n-1) * n

# print(fact(5))

n = int(input("Enter a number : "))
def fact(n):
    if(n==0 or n ==1):
        return 1
    else:
        return fact(n-1) * n

print(fact(n))