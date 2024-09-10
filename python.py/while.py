# print numbers from 1 to 100.
"""count = 1
while count <=100:
    print(count)
    count +=1"""

#print numbers from 100 to 1.
"""count = 100
while count >=1:
    print(count)
    count -=1"""

#print the multiplication table of a number n.
"""n=int(input("Enter your number : "))
i=1 
while i<=10:
    print(n*i)
    i +=1"""

# print the elements of the following list using a loop.
# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<=len(nums):
#     print(nums[i])
#     i +=1

# search for a number x in this tuple using loop.
"""num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter your numbers : "))
i=0
while i<len(num):
    if(num[i]==x):
        print("The number entered by you is found at indx",i)
    i +=1"""
#Break
"""i=1
while i <=10:
    if(i==7):
        break
    print(i)
    i +=1"""

#Continue // Even or odd number 
"""i=1
while i <=10:
    if( i%2 !=0 ):
        i += 1
        continue
    print(i)
    i +=1 """

# For Loop 

"""list = [1,2,3]
for el in list:
    print(el)

tup = (1,4,5,7,97,7)
for num in tup:
    print(tup)"""

"""n=input("Enter a string : ")
for name in n:
    print (n)"""

"""str = "Aashish"
for char in str:
    print(char)
else:
    print("End")"""

# WAP to find sum of first n numbers.

n=int(input("enter a number : "))

sum=0
for i in range(1,n+1):
    sum += i
print("sum of number is : ",sum)