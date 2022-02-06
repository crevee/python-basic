print(5)
print(3* (3-10))
print("z" *9)

#참 / 거짓  boolean

print( 5> 10)


# 애완동물을 소개해 주세요~

animal = "강아지"
name = "멍뭉이"
age =  4
hobby = " 산택"
is_adult = age >= 3


print("우리집" + animal + "의 이름은 " + name + "예요")
print(name + " 는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요? " ,(is_adult))

# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수 값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : XX 행 열차가 들어오고 있습니다.

station = "사당"

print(station + "행 열차가 들어오고 있습니다.")

print(2**3)
print(5%3)
print(5/3)
print(5//3)

print(abs(-5)) #5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) #3

from math import *

print(floor(4.99)) # 내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) # 제곱근 4

from random import *

print(random ()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10) + 1)

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성

#Quiz 2) 당신은 최근 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인
#아래 조건에 맞은 오프라인 날짜를 정해주는 프로그램을 작성
# 조건 1) 랜덤으로 날짜를 뽑아야 함
# 조건 2) 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건 3) 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외

# 출력문 예제) 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

day = randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월 " + str(day)
+ "일로 선정 되었습니다.")

sentence = "나는 작업중"
print(sentence)
sentence1 = """
주말에도
작업중
"""
print(sentence1)

jumin = "990512-1234567"
print("성별 : " + jumin[7])
print("년 : " +jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서부터) : " +jumin[-7:])

titlename = "Python is Amazing"
print(titlename.lower())
print(titlename.upper())
print(titlename[0].isupper())
print(len(titlename))
print(titlename.replace("Python", "Java"))

index = titlename.index("n")
print(index)

#index -> 오류 find -> -1 값이 없는 경우

print(titlename.count("n"))

print("나는 %d 살입니다." %20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." %"A")
print("나는 %s색과 %s 색을 좋아해요." % ("파란" , "빨간"))

print("나는 {}살입니다." .format(20)) #{1},{0} 순서변경 가능

print("나는 {age}살이며, {color}색을 좋아해요. " .format(age = 20, color ="빨간"))

# \n : 줄바꿈
print("저는 \"테스터\"입니다. ")

# \\ : 문장 내에서 \
# \r : 커서를 맨 앞으로 이동
print("Red Apple \rPine")

#\b : 백스페이스 (한 글자 삭제)
#\t : 탭

#Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙 1 : http:// 부믄은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"
# 결과 예시) 생성된 비밀번호는 : nav51!

testurl = "http://www.google.com"
my_str = testurl.replace("http://www.", "")
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지

testpassword = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(testurl + "의 생성된 비밀번호는 : " + testpassword)
