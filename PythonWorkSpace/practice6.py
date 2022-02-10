def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance+ money))
    return balance + money

def withdraw(balce, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance- money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금 수수료
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1} 원입니다. ".format(commission, balance))


########### 기본값 #########

def profile(name, age , main_lang ="파이썬"): # 기본값
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("우히히", 20, "파이썬")
profile("키키", 25, "자바")
profile(main_lang="C++", name="코코콩", age= 15) # 키워드 값

#가변인자

def profile_test(name, age, *language):
    print("이름 : {0} \t 나이 : {1} \t".format(name, age), end =" ")
    for lang in language:
        print(lang, end= " ")
    print()

profile_test("쿠하하", 20, "Pyhton", "Java", "C", "C++", "C#", "JavaScript")
profile_test("김김김", 25, "Kotlin", "Switft")


# 지역변수와 전역변수

gun_num = 10

def checkpont(soldiers): #경계 근무
    global gun_num # 전역 공간에 있는 gun_num 사용
    gun_num = gun_num - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun_num))

def checkpoint_return(gun_num, soilders):
    gun_num = gun_num - soilders
    print("[함수 내] 남은 총 : {0}".format(gun_num))
    return gun_num


print("전체 총 : {0}". format(gun_num))
# checkpont(2) # 2명이 경계 근무 나감
gun_num = checkpoint_return(gun_num, 2)
print("남은 총 : {0}".format(gun_num ))


# 퀴즈) 표준 체중을 구하는 프로그램
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# * 함수명 : std_weight
# * 전달값 : 키(height), 성별 (gender)
# 조건 2 : 표준 체중은 소수점 둘쨰자리까지 표시

#출력 예) 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21
    else:
        print("다시 입력해주세요.")


height = input("키를 입력해주세요 ex)175 : ")
gender = input("성별을 입력해주세요. ex)남자 : ")
weight = round(std_weight(int(height)/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))