#표준 입출력

from multiprocessing.connection import answer_challenge


print("Python", "Java", sep="과", end="?")
print("무엇이 더 재밌을까요?")

#import sys
#print("Python", "Java", file=sys.stdout)
#print("Python", "Java", file=sys.stderr)

#시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽정렬, 오른쪽 정렬

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  #3자리까지 빈자리 0으로 채움

answer = input("아무값이나 입력해주세요. : ") 
#사용자 입력으로 값을 입력받으면 문자열 string으로 받는다.

print("입력하신 값은 " + answer + "입니다.")

#빈 자리는 빈공간으로 두고, 오른족 정렬을 하되, 총 10자리 공간을 확보

print("{0: >10}".format(500))

#양수일 떈 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))

# 3자리 마다 콤마를 찍고 +-부호도 붙이기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))

#빈자리 ^로 채우기
print("{0:^<+30,}".format(1000000000))

#소수점 특정 자리수 까지만 표시

print("{0:.2f}".format(5/3))

