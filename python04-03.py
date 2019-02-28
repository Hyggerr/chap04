#-*-coding:utf-8

print("# 파일 입출력")
# 파이썬에서 파일을 읽을 때 사용한는 명령어 open
# open(파일명, 사용모드)
# 사용모드 : r(읽기모드), w(쓰기모드), a(추가모드)
# 맥이나 리눅스 같은 경우는 파일 경로 시스템이 다름
# 드라이브라는 개념이 없고 모두 디렉토리로 구성되어 있음
# 파이썬 3버전 대에서 유니코드 파일 읽는 방법
# open 함수는 지정한 파일을 열때 사용하는 명령어
# 첫번째 매개변수는 파일의 경로와 파일명을 입력함
# 현재 실행파일 같은 위치에 파일이 있을 경우는 경로를 무시해도 됨
print("# 첫 줄 읽기")
# f = open("C:/study/python/chap04/test.txt", "r", encoding="utf8")
f = open("test.txt", "r", encoding="utf8")
# 파일에서 내용 한줄을 읽어옴
line = f.readline()
# 읽어온 내용 출력
print(line)
# 열었던 파일을 닫아줘야함 (닫지 않으면 메모리 누수현상 발생)
f.close()

# 파이썬 2버전 대에서 유니코드 파일 읽는 방법
# print("# 첫 줄 출력")
# f = open("C:/study/python/chap04/test.txt", "r")
# line = f.readline()
# line.decode("utf8")
# print(line)
# f.close()

print("# 모두 읽기")
# f = open("C:/study/python/chap04/test.txt", "r", encoding="utf8")
f = open("test.txt", "r", encoding="utf8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

print()
print("# 쓰기 모드")
f = open("test.txt", "w", encoding="utf8")
for i in range(1, 11):
    data = "{0}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()

print()
print("# 모두 읽기")
# f = open("C:/study/python/chap04/test.txt", "r", encoding="utf8")
f = open("test.txt", "r", encoding="utf8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()