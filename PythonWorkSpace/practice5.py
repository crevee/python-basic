#continue 와 break

absent =[2, 5] #결석한 학생 번호
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지 {0}는 교무실로 따라와".format(student))
        break;
    print("{0}번 책 읽어봐".format(student))


# 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

student_num = [1, 2, 3, 4, 5]
print(student_num)
student_num = [i+100 for i in student_num]
print(student_num)

Enemy_name = ["코코아", "초코", "아아리스"]
Enemy_name = [len(i) for i in Enemy_name]
print(Enemy_name)

#대문자로 변환
#Ex) students = [i.upper() for i in students]

#퀴즈) 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
# 조건 1) 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수
# 조건 2) 당신은 소요 시간이 5분 ~ 15분 사이의 승객만 매칭

#(출력문 예)
#[0]  1번째 손님 ( 소요시간 : 15 분)
#[ ]  2번째 손님 ( 소요시간 : 50 분)
#...
#[ ] 50번쨰 손님 ( 소요시간 : 16 분)

#총 탑승 승객 : 2분

from random import *
count_passanger = 0 # 총 탑승 승객 수

for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51)
    if 5<= time <=15: # 매칭 성공
        print("[0]  {0}번째 손님 (소요시간 : {1}분".format(i, time))
        count_passanger +=1
    else: # 매칭 실패
         print("[ ]  {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 : {0}".format(count_passanger))
