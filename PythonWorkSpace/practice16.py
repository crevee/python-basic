import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# import travel.thailand.ThailandPackage <- 오류 발생

#from travel.thailand import ThailandPackage <- 사용 가능

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()


from travel import * # *사용시 __init__.py 에서 __all__ = ["vietnam"] 생성해야함


import inspect
import random
print(inspect.getfile(random)) #random 모듈 위치를 알려줌
