# Create a class called order which stores item & its price.
# use dunder function __gt__() to convey that:
    # order1>order2 if price of order1>price of order2

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        #return self.price > odr2.price
        return self.price < odr2.price

odr1 = order("Chips",20)
odr2 = order("mithai",25)

print(odr1 > odr2)
print(odr1 < odr2)


   