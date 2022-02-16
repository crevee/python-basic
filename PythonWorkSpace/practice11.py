class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyAbleUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__() # Flyable 생성자만 상속
        Unit.__init__(self)
        Flyable.__init__(self) # __init__ 을 사용하여야 다중상속시 다나옴

# dropship

dropship = FlyAbleUnit()