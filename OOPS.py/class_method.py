# class person:
#     name = "anonymous"

#     # def cahngename(self,name):
#     #     self.name = name #person
#     #     #self.__class__.name = "Aashish"

#     @classmethod
#     def changename(cls,name):
#         cls.name = name

# p1 = person()
# p1.changename("Sahil Kumar")
# print(p1.name)
# print(person.name)


class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage = str((self.phy + self.chem +self.math) / 3) +" % "#percentage

    # def calcpercentage(self):
    #     self.percentage = str((self.phy + self.chem +self.math) / 3) +" % "

    @property
    def percentage(self):
        return str((self.phy + self.chem +self.math) / 3) +" % "

stu1 = student(98,64,87)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)
