#theater_module.py 를 사용

import theater_module #모듈 불러옴

theater_module.price(3) # 3명이서 영화 보러 갔을 떄 가격
theater_module.price_morning(4)

import theater_module as mv #모듈명이 긴 경우 줄여씀
mv.price_morning(5)

from theater_module import *

from theater_module import price, price_morning

from theater_module import price_soldier as ps

