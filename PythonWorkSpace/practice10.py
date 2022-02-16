
# 공격 유닛 생성
#name = "대장유닛"
#hp = 100
#damage = 5

#print("{0} 유닛이 생성되었습니다.".format(name))
#print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 전차 유닛 생성
#tank_name = "K1A2"
#tank_hp = 150
#tank_damge = 40

#print("{0} 유닛이 생성되었습니다.".format(tank_name))
#print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damge))


#def attack(name, location, damage):
#    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

#attack(name, "1시", damage)
#attack(tank_name, "1시", tank_damge)

class Unit:
    def __init__(self, name, hp, damage, speed):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

marine1 = Unit("마린", 40, 5, 0)
marine2 = Unit("마린" ,40 ,5, 0)
tank = Unit("탱크", 150, 35, 0)

wraith1 = Unit("레이스", 80, 5, 0)
print("유닛 이름 : {0}, 공격력:  {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit(" 뺴앗은 레이스", 80, 5, 0)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self,name, hp, damage, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1= AttackUnit("파이어뱃", 50, 16, 0)
firebat1.attack("5시")

#공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스 (AttackUnit과 Flyable을 상속받음)
class  FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
battlecruiser.move("9시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()       
game_over() #pass 사용 예시



#건물

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__initt__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

# 서플라이 디폿 : 건물 , 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

