#제어문

weather =  input("오늘 날씨는 어떤가요? ")

if weather == "비" or "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지" :
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")

Today_temperature = int(input("온도는 어떤가요? "))
if 30 <= Today_temperature:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= Today_temperature <30:
    print("괜찮은 온도에요.")
elif 0<= Today_temperature <10:
    print("외투를 챙겨주세요.")
else:
    print("집에 있는걸 추천해요.")
