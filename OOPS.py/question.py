# create student class that takes name & marks of 3 subjects as arguments in constructor. THen create a method to print the average.


# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("Hi",self.name, "Your average marks is:",sum/3)

# s1 = student("Aashish", [88, 89, 98])
# s1.avg_marks()


# Create Account calss with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.account_no = acc
        self.balance = bal

    # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("Total balance = ",self.get_balance())

    # credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount, "was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
       return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(30000)
acc1.debit(2000)
