#-*-coding:utf-8

# 연습문제 1
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for n in range(0, 1000):
    print(fib(n))

# 연습문제 2
f = open("sample.txt", "r", encoding="utf8")
lines = f.readlines() # 파일을 한줄씩 모든 내용을 읽음
# 리스트에 읽은 내용을 모두 반환
# 파일에서 읽은 내용은 모두 문자열 타입임
f.close()

total = 0
for line in lines:
    score = int(line) # 문자열 타입을 숫자형 타입으로 반환
    total += score

average = total / len(lines)

f = open("result.txt", "w", encoding="utf8")
f.write(str(average))  # 파일에 내용을 쓸때 모두 문자열 타입으로 써야함
f.close()

# 문제 3) 파일을 열고, 메뉴에 따라서 파일의 내용을 확인하고 파일의 
#   내용을 입력하는 형태의 프로그램을 작성하세요.
# 파일명 : memory.txt
# 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 3. 종료
# 내용 입력 시 기존 내용을 덮어쓰기하는 형태로 작성
while True:
    num = input("문3) 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 3. 종료\n메뉴를 입력하세요: ")
    num = int(num)
    if num == 1:
        f = open("memory.txt", "w", encoding="utf8")
        content = input("내용을 입력하세요: ")
        f.write(content)
        f.close()
    elif num == 2:
        f = open("memory.txt", "r", encoding="utf8")
        lines = f.readlines()
        f.close()
        for line in lines:
            print(line)
    elif num == 3:
        print("종료")
        break

# 문제 4) 위의 문제 3번을 함수를 이용하여 프로그램을 작성하세요
# 내용 입력 함수명 memoryWrite
# 내용 출력 함수명 memoryRead
# 다른 사항은 문제 3번과 동일

def memoryWrite():
    f = open("memory.txt", "w", encoding="utf8")
    content = input("내용을 입력하세요: ")
    f.write(content)
    f.close()

def memoryRead():
    f = open("memory.txt", "r", encoding="utf8")
    lines = f.readlines()
    f.close()
    for line in lines:
        print(line)

while True:
    num = input("문4) 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 3. 종료\n메뉴를 입력하세요: ")
    num = int(num)
    if num == 1:
        memoryWrite()
    elif num == 2:
        memoryRead()
    elif num == 3:
        print("종료")
        break
