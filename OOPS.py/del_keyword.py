# Delete keyword in python

# class student:
#     def __init__(self,name):
#         self.name = name
    
# s1 = student("Aashish")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private attributes & methods

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")
print(acc1.acc_no)

print(acc1.reset_pass())
