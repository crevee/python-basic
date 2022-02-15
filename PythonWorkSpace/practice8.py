#파일 입출력 입력 방법 1)

#score_file = open("score.txt", "w", encoding = "utf8")
#print("수학 : 0", file = score_file)
#print("영어 : 50", file=score_file)
#score_file.close()

#파일 입출력 입력 방법 2)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n 코딩 : 100")
score_file.close()

#파일 입출력 출력 방법 1)
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

#파일 출력 방법 2) 한줄한줄
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
score_file.close()

#파일 출력 방법 3) while 문 사용
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line :
        break
    print(line)
score_file.close()

#파일 출력 방법 4) list 형태로 저장

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()