#for

for wating_no in range(5):
    print("대기번호 : {}".format(wating_no))

starbucks_guest = ["아이잉", "토잉", "코르릉"]

for cusmtomer in starbucks_guest:
    print("{}님 커피가 준비되었습니다.".format(cusmtomer))


#while

Coffebin_customer = " 우앙"
index = 5
while index >= 1:
    print("{0}님 커피가 준비되었습니다. {1}번 안에 찾으러 와주세요.".format(Coffebin_customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기되었습니다.")

################################

Person ="Unknown"

while Person != Coffebin_customer:
    print("{0}, 커피가 준비 완료되었습니다. ".format(Coffebin_customer))
    print = input("이름이 어떻게 되세요?")
