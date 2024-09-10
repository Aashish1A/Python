# Create a file "practice.txt" using python. Add the following data in it.

# with open("practice.txt","w") as f:
#     data = f.write("Hi everyone""\nwe are learning File i/o""\nusing java""\ni like programming in java")
#     print(data)

# WAP that replaces all occurences of "java" with "python" in above file.

# with open("practice.txt","r") as f:
#     data=f.read()

# new_data = data.replace("java","python")
# print(new_data)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# with open("practice.txt","w") as f:
#     data=f.write(new_data)
#     print(data)

# Search if the wors "learning" exist in the file or not.
    
"""with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")):
        print("The data is found")
    else:
        print("The data is not found")
  

def check_word():
    with open("practice.txt","r") as f:
        data=f.read()
    if(data.find("learning")):
        print("The data is found")
    else:
        print("The data is not found")
   

check_word()"""

# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found,

# def check_line():
#         word = "learning"
#         data = True
#         line_no = 1
#         with open("practice.txt","r") as f:
#             while data:
#                 data=f.readline()
#                 if(word in data):
#                     print(line_no)
#                     return
#                 line_no += 1
#         return -1
# check_line()

# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("ak.txt","r") as f:
    data=f.read()
    print(data)

    nums = data.split(",")
    for cal in nums:
        if(int(cal) % 2==0):
            count+=1
print(count)

    
