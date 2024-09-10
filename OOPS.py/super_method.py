class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("cat started")

    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("pirus","electric")
print(car1.type)
