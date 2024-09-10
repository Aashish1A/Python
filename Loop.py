          # Same Logic in all question
          
# WAP to print all number on different lines.
# n=int(input("Enter the number : "))
# m=n
# while m!=0:
#     d=m%10
#     print(d)
#     m=m//10

# Write a program to check whether the number is palindrome or not.

n=int(input("Enter the number : "))
sum=0
m=n
while m!=0:
    d=m%10
    sum=sum*10+d
    m=m//10
if sum==n:
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")

# Write a program to check whether the number is Spy or not.

"""n=int(input("Enter the number : "))
m=n
sum=0;prod=1
m=n
while m!=0:
    d=m%10
    sum=sum+d;prod=prod*d
    m=m//10
if sum==n:
    print("The number is Spy.")
else:
    print("The number is not Spy.") """

        # something same in all program

# WAP to find factorial of a number.

"""n=int(input("Enter the number : "))
for i in range(1,n+1):
    if n%i==0:
        print(i) """

# Write a program to check whether the number is prime or not.

"""n=int(input("Enter the number : "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("The number is prime number.")
else:
    print("The number is not a prime number.")"""

# Write a program to check whether the number is composite or not.

"""n=int(input("Enter the number : "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count>2:
    print("The number is composite number.")
else:
    print("The number is not a composite number.")"""

# Write a program to check whether the number is perfect or not.

"""n=int(input("Enter the number : "))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("The number is perfect number.")
else:
    print("The number is not a perfect number.")"""

# Write a program to check whether the number is Abundant or not.

"""n=int(input("Enter the number : "))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("The number is abundant number.")
else:
    print("The number is not a abundant number.")"""

# Write a program to print Table of any number.

"""n=int(input("The multiplication Table of : "))
for count in range(1,11):
    print(n,"x","=",n*count)"""

# Wap to print the numbers from 1 to 10.

"""for i in range (1,11):
    print(i) """

# Wap to print all even numbers from 1 to 20 using loop.

"""for i in range(1,21):
    if i%2==0:
        print(i)"""

# Create a while loop that counts from 1 to 10 and prints the numbers.

"""count=1
while count<=10:
     print(count)
     count+=1 """

# WAP that prints the reverse of a user entered string using a for loop.

"""n=input("Enter any character : ")
l=n.split()
l.reverse()
print("Reversed character :",end=" ")
for i in l:
    print(i,end=" ")"""

# WAP that calculates the sum of all numbers from 1 to 30 using for loop.

""" sum=0
for i in range (1,31):
    sum+= i
    print(sum) """

# using a for loop print first 10 multiples of 5.

# for i in range (1,11):
#     print(5*i) 

# Create a program that asks the user enter a number and uses a while loop to find and
  #print the sum of all numbers from 1 to that number.

"""num=int(input("Enter the number : "))
count=1
while count<=num:
    print(count)
    count+=1"""

# Create a while loop that asks the user to enter a number and keep asking until the user enters the number 7.

"""while True:
    user_input=int(input("Enter the number : "))
    if user_input==7:
        break """

# WAP that prints the fibonacci sequence up to the 10th term using a for loop.








# WAP that accepts the a word from the user and reverse it.

""""a = input("Enter a word to reverse : ")
for char in range(len(a)-1,-1,-1):
    print(a[char],end="")"""

# 





