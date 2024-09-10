def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) + n

print(calc_sum(5))

# Write a recursive function to print all elements in a list.

# def print_list(list,indx=0):
#     if(indx == len(list)):
#         return
#     print(list[indx])
#     print_list(list,indx+1)

# fruits = ["mango","banana","apple","lichi"]
# print_list(fruits)
        

   