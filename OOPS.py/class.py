# class student:
#     college_name = "Apna college"
#     name = "anonymous" # class attributes

#     def __init__(self,fullname,marks):
#         self.name = fullname # obj attr > class attr 
#         self.marks = marks
#         print("Adding new student in database..")

# s1 = student("Aashish", 98)
# print(s1.name, s1.marks)

# s2 = student("Aditya", 87)
# print(s2.name, s2.marks) 

# print(s2.college_name)

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Welcome student",self.name)

    def get_marks(self):
        return self.marks

s1 = student("Aashish",98)
s1.hello()
print(s1.get_marks())
