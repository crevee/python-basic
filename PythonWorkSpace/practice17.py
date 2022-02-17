#pip install

#구글에서 pypi 검색하여 프로젝트 탐색

# 터미널에서 입력 pip install beautifilsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#pip list 사용시 설치된 것 보여줌
#pip show beatifulsoup4 beatifulsoup4에 대한 정보를 알려줌
#pip uninstall beatifulsoup4  <- 지우기


# 내장 함수
# input : 사용자 입력을 받는 함수
# dir : 객체가 어떤 변수와 함수를 가가지고 있는지 표시

import random
print(dir(random))

name = "Jun"
print(dir(name))

#외장함수 <- import 해야함
# glob : 경로 내의 폴더/ 파일 목록 조회 (윈도우 dir)

import glob
print(glob.glob("*.py"))

#os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir())

#time : 시간 관련 함수

import time

print(time.strftime("%Y-%m-%D %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today+ td) # 오늘부터 100일 후