#예외처리

class BigNumberError(Exception): #에러 임의로 하나 만들어줌
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요. : "))
    num2 = int(input("두 번째 숫자를 입력하세요. : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except Exception as err:
    print(err)      #모든 에러시 나오게함5


try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2>= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") #최종적으로 실행됨
