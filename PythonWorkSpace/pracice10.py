
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
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린" ,40 ,5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력:  {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit(" 뺴앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name, hp, damage)
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

firebat1= AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)

class Flyable:
    def __init___(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스 (AttackUnit과 Flyable을 상속받음)
class  FlyableAttackunit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__initt_(self, flying_speed)
