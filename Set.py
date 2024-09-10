"""collection = {1,2,3,5,6,7,"world",8,67}

print(collection)
print(len(collection)) # total no of items"""

#for empty set

"""collection = set()
print(type(collection))"""

# Set methods

"""set = {1,2,3,4,5,8,"hello","Aashish"}

set.add("98")
print(set)

set.remove("hello")
print(set)

set.clear()
print(set)

set = {"vickey","hello","Aashish"}
print(set.pop())
print(set)"""

"""set1 = {1,2,3,4,7,9}
set2 = {3,7,9,4,1}
print(set.union(set2))
print(set1)

set1 = {1,2,3,4,7,9}
set2 = {3,7,9,4,1}
print(set1.intersection(set2))"""

# Figure out a way to store 9 & 9.0 as separate values in the set.

values = {9,"9.0"}
print(values)

# wap to create a symmetric difference.

"""set1 = {1,2,3,4,8,7,9}
set2 = {3,7,9,4,1}
print(set1.difference(set2))

set1 = {1,2,3,4,8,7,9}
set2 = {3,7,9,4,1}
print(set1.symmetric_difference(set2))
print(len(set1))"""

#Wap to find the maximum and minimum value in a set.

#set1 = {1,2,3,4,8,7,9}
#print(max(set1))
#print(min(set1))


"""a = int(input("entner a number : "))
set1 = {1,2,3,4,8,7}
if(set1==set1):
    print("%d","is present in both")
else:
    print("%d","number is not present")"""

#  wap to print third largest from a list.

def third_largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[2]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))

    

