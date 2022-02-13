#pickle

import pickle

#profile_file = open("profile.pickle", "wb")
#profile = {"이름" : "우히하하하", "나이": 20, "취미":["축구", "골프", "코딩"]}
#print(profile)
#pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
#profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#with


#with open("profile.pickle", "rb") as profile_file_with:
#    print(pickle.load(profile_file_with))

#with를 사용하여 file에 저장하기

#with open("study.txt", "w", encoding="utf8") as study_file:
#    study_file.write("파이썬을 배우는 중")

#with를 사용하여 file 내용 불러오기

#with open("study.txt", "r", encoding="utf8") as study_file:
#    print(study_file.read())

#Quiz) 매주 1회 작성해야 하는 보고서로 아래와 같은 형태
# - X 주차 주간보고 - 
# 부서 :
# 이름 :
# 업무요약 :

# 1주차부터 50주차까지의 보고서 파일을 만든느 프로그램을 작성
# 조건) 파일명은 '1주차.txt', '2주차.txt', ... 와 같다.

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.wrtie("\n이름 : ")
        report_file.write("\n업무 요약 : ")

qq
