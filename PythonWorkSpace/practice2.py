

# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

subway.append("하하")
print(subway) #추가하기

#정형돈씨를 유재석 /조세호 사이에 추가

subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명 씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름이 몇 명 있는지 확인
print(subway.count("유재석"))

# 정렬도 가능

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용

num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]


#리스트 확장

num_list.extend(mix_list)
print(num_list)

#사전

cabinet = {3:"우히히", 100:"우다다"}
print(cabinet[3]) # 없는경우 종료

print(cabinet.get(3)) # 없는경우 None
print(cabinet.get(5, "사용 가능")) #값이 없는 경우 "사용 가능" 출력

#새 손님
print(cabinet)
cabinet["C-20"] = "히히히"
del cabinet["C-20"]

print (cabinet)
print (cabinet.keys())
print (cabinet.values())
print (cabinet.items())

cabinet.clear

#튜플 (속도가 리스트보다 빠름, 값 변경 불가)

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("고구마까스") <- 튜플에 값 추가 불가

(name, age, hobby) = ("고고미", "20", "게임")
print(name, age, hobby)

#집합 (set) 중복 안됨, 순서 없음

my_set = {1,2,3,3}
print(my_set)


java_programmer = {"가가", "나나", "다다"}
python_programmer = set(["가가", "노노", "도도"])

#교집합 (java 와 python을 모두 할 수 있는 개발자)
print(java_programmer & python_programmer)
print(java_programmer.intersection(python_programmer))

#합집합
print(java_programmer | python_programmer)
print(java_programmer.union(python_programmer))

#차집합 (java는 가능하나 python은 불가능한 개발자)
print(java_programmer - python_programmer)
print(java_programmer.difference(python_programmer))

#python 할 수 있는 사람이 늘어남
python_programmer.add("기누")
print(python_programmer)

#java 하는 법을 잊음
java_programmer.remove("다다")
print(java_programmer)

#자료구조의 변경

Cafe_menu = {"커피", "우유", "주스"}
print(Cafe_menu, type(Cafe_menu))

Cafe_menu = list(Cafe_menu)
print(Cafe_menu, type(Cafe_menu))

Cafe_menu = tuple(Cafe_menu)
print(Cafe_menu, type(Cafe_menu))

# Quiz) 댓글 작성자중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 조건1 : 편의상 댓글은 20명이 작성, 아이디는 1 ~ 20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

#출력 예시
#-- 당첨자 발표 --
#치킨 당첨자 : 1
#커피 당첨자 : [2, 3, 4]
#-- 축하합니다 --

#활용 예제
from random import *
Ex_list = [1,2,3,4,5]
print(Ex_list)
shuffle(Ex_list)
print(Ex_list)
print(sample(Ex_list, 1))


Id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Id_list = range(1, 21) 1~ 20까지 숫자를 생성
# Id_list = list(Id_list) <- range에서 list로 형변환

print("-- 당첨자 발표 --")
shuffle(Id_list)
Winner_list = sample(Id_list, 4)
print("치킨 당첨자 : {}".format(Winner_list[0]))
print("커피 당첨자 : {}".format(Winner_list[1:]))
print("-- 축하합니다. --")