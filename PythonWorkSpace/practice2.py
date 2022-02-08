

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