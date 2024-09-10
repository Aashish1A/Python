# n = int(input("Enter a number : "))
# def find_oddeven(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# find_oddeven(n)

num= [3,6,3.2,6.2,23,6,2,67,34,63]
n = int(input("Enter a number : "))
def find_num(n):
    if n in num:
        print("Number is found")
    else:
        print("Number is not found")

find_num(n)