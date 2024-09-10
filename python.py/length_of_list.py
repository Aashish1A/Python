# WAP to print the length of a list.

"""num=[3,23,4,2,1,5,4,6,3]
def calc_len(list):
    print(len(list))

calc_len(num)"""

# wap to print the elements of a list in a single line.
"""num = [2,4,6,7,8,95,3,2]
def print_len(num):
    print(num)

print_len(num)"""

# num = [2,4,6,7,8,95,3,2]
# def print_num(list):
#     for num in list:
#         print(num, end=" ")
# print_num(num)

# WAP to find factorial of number n.

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)

calc_fact(5)
