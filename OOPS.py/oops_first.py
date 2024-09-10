# Object oriented programming in python

# class student:
#     def __init__(self):
#         print("Adding new student in database..")
#     name = "Aashish Kumar"

# s1 = student()
# print(s1.name)


# class car:
#     color = "Blue"
#     brand = "Mercedies"
# car1 = car()
# print(car1.color)
# print(car.brand)

class student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student in database..")

s1 = student("Aashish", 98)
print(s1.name, s1.marks)

s1 = student("Aditya", 87)
print(s1.name, s1.marks)