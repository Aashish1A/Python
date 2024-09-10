# Print the elements of the following list using a loop.

"""list = [1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)"""

# Search for a number x in this tuple using loop.

"""num=(1,4,9,16,25,36,49,64,81,100)
x=input("Enter your numbers : ")
for num in x:
    if(num == x):
        print("Number is found")
        break
    else:
        print("number is not found")"""
   
num=(1,4,9,16,25,36,49,64,81,100)
x=81
indx = 0
for el in num:
    if(el == x):
        print("Number is found at index",indx)
    indx += 1