        # Some Question on List


# Create a list and print the items of list..

"""a=[1,2,3,"Aashish","Blue",8,9]
print(a)
print(type(a))"""
     # List Indexing & Slicing

"""a=[1,2,5,7,9,"Anish","blue","Red",3]
print(a[0])
print(a[-2])
print(a[4])
print(a[1:3:5])
print([len(a)])"""

     # List Method

"""list1=[1,2,3,"aashish","a",3,8.8,"red","Blue"]
print(len(list1))

list1.append("Ankit")
print("New list : ",list1 )

list1.remove("aashish")
print("New list : ",list1 )

list1.index(8.8)
print("New list : ",list1 )

list2=["Chunnu"]
list1.extend(list2)
print("New list : ",list1 )

list1.count(3)

list1.reverse()
print("New list : ",list1 )

list1.pop(1)
print("New list : ",list1 )"""

"""student=["karan",86,"df",44,546,"fdg"]
student[5]="Aashish"
print(student[-3:-1])"""

#wap to ask the user to enter names of their 3 favorite movies & store them in a list.
"""list=[]
list1=input("enter your 1st favourite movies : ")
list2=input("enter your 2nd favourite movies : ")
list3=input("enter your 3rd favourite movies : ")
list.append(list1)
list.append(list2)
list.append(list3)
print(list)"""



#wap to check if a list contain a palindrome of elements. use copy method
#[1,2,3,2,1] [1,"abc","abc",1]

list=[1,2,2,1]
copy=list.copy()
copy.reverse()

if(copy==list):
    print("palindrome")
else:
    print("not palindrome")
