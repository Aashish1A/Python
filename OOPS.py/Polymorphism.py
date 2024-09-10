# print (1+2)
# print("Aashish" + "college") # concatenate
# print((1,2,3) + (4,5,6)) # Merge
# print(type((1,2,3)))

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2): #Dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)
    
    def __sub__(self,num2): #Dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal, newImg)
    
    def __mul__(self,num2): #Dunder function
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return complex(newReal, newImg)
    
    def __truediv__(self,num2): #Dunder function
        newReal = self.real / num2.real
        newImg = self.img / num2.img
        return complex(newReal, newImg)
    
    def __mod__(self,num2): #Dunder function
        newReal = self.real % num2.real
        newImg = self.img % num2.img
        return complex(newReal, newImg)
    
num1 = complex(1,3)
num1.showNumbers()

num2 = complex(5,6)
num2.showNumbers()

#num3 = num1.add(num2)
num3 = num1 + num2
num3.showNumbers()

num4 = num1 - num2
num4.showNumbers()

num5 = num1 * num2
num5.showNumbers()

num6 = num1 / num2
num6.showNumbers()

num7 = num1 % num2
num7.showNumbers()