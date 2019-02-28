#-*-coding:utf-8

print("# 함수 사용하기")
# 함수는 소스의 재활용을 위해서 사용
# 함수를 나타내는 키워드 def 를 사용
# 반환 타입 선언이 함수의 원형에 없음
# 함수의 매개 변수 선언 시 매개 변수의 타입을 입력할 필요 없음

# 함수의 사용법

# 자바에서의 함수 원형
# public void 함수명(int 매개변수){
    # 실행코드
    # return 반환값
# }

# 파이썬에서의 함수 원형
# def 함수명(매개변수):   # (차이점)반환 타입이 없음  # 매개변수 타입도 없음
    # 실행 코드
    # return 반환값

# def sum(a,b):
#     return a+b

def sum(a, b):
    result = a + b
    return result

a = 3
b = 4
c = sum(a,b)
print(c)

print(sum(8, 9))

def func1():
    print("매개변수와 반환값이 없는 함수")
def func2(a, b):
    print("반환 값이 없고, 매개변수가 {0}, {1} 인 함수".format(a, b))
def func3():
    print("매개변수가 없고 반환값만 있는 함수")
    return "함수 3번"
def func4(a, b):
    print("매개 변수가 {0}, {1} 이고, 반환값이 있는 함수".format(a, b))
    return "함수 4번"
print()
func1()
func2(10, 20)
x = func3()
print(x)
y = func4(10, 20)
print(y)

print()
print("# 문제 1) 매개 변수 2개를 입력 받고 계산된 값을 반환하는 총 4개의 함수를 생성하여 계산기 프로그램을 작성하세요")
# 함수명 : plus, minus, multi, divide
def plus(a, b):
    return ("{0} + {1} = {2}".format(a, b, a + b))
def minus(a, b):
    return ("{0} - {1} = {2}".format(a, b, a - b))
def multi(a, b):
    return ("{0} * {1} = {2}".format(a, b, a * b))
def divide(a, b):
    return ("{0} / {1} = {2}".format(a, b, a / b))
print(plus(10, 20))
print(minus(10, 20))
print(multi(10, 20))
print(divide(10, 20))
print(divide(100, 20))

print()
# 함수의 매개 변수가 몇개인지 모를 경우 함수 선언 방법
# 매개 변수의 이름 앞에 * 기호를 붙여서 선언
# 파이썬에서는 함수 오버로딩을 지원하지 않기 때문에 매개변수에 * 기호를 사용하여 
# 매개 변수를 튜플로 받고 그 튜플의 데이터 타입과 길이를 확인하여 오버로딩을 구현한다

# 매개변수로 튜플을 받았다고 생각하면 쉬움
print("# 여러개의 입력값을 받는 함수")
def sum_many(*args):
    sum = 0
    for i in args: # 매개변수의 수 대로 값을 뽑아냄
        sum += i
    return ("sum : {0} = {1}".format(args, sum))
print(sum_many(1, 2, 3, 4, 5))
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)
print("매개 변수가 1개인 sum_many 의 합: {0}".format(sum_many(1)))
print("매개 변수가 2개인 sum_many 의 합: {0}".format(sum_many(1,2)))
print("매개 변수가 3개인 sum_many 의 합: {0}".format(sum_many(1,2,3)))
print("매개 변수가 4개인 sum_many 의 합: {0}".format(sum_many(1,2,3,4)))
print("매개 변수가 5개인 sum_many 의 합: {0}".format(sum_many(1,2,3,4,5)))

print()
print("# sum_mul")
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return ("{0} : {1} = {2}".format(choice, args, result))

result = sum_mul("sum", 1,2,3,4,5)
print(result)
result = sum_mul("mul", 1,2,3,4,5)
print(result)

print()
# 기존 언어에서 반환값은 1개만 반환이 가능함
# 기존 다른 언어에서는 반환값을 2개 이상 받기 위해서 배열 및 리스트와 같은 자료구조를
# 사용하여 값을 반환받음
# public int sum_and_mul(a,b){
#   int[] result = [a=b, a*b]
#   return result
# }
# 파이썬에서는 반환값을 튜플로 받아 2개 이상 반환할 수 있음(사실 1개의 반환값임)
print("# 반환값은 언제나 하나이다")
def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
# 튜플 result = (a+b, a*b) 와 같음
print(result)

print()
# 아래와 같은 형태는 불가능
# return 문은 2개의 기능이 있음
# 함수를 실행하고 그 결과값을 함수를 호출한 시점으로 반환하는 것
# return 문을 만나면 그 즉시 해당 함수를 종료함
print("# return 2개는 불가능")
def sum_and_mul1(a,b):
    return a+b
    return a*b # return 윗라인에서 return 문을 실행하였기 때문에 함수의 실행이 
    # 완전 종료되어 아래의 return 문을 실행할 수 없음

print()
# 함수를 실행 할 때 필요한 매개변수에 사용자가 모든 값을 입력하는 형태가 아니라
# 기본적으로 필요한 값을 미리 지정해 놓고 사용자가 입력하지 않았을 경우에만 초기값으로
# 매개 변수가 초기화되어 함수를 실행하는 형태#
# 초기값이 지정된 매개변수는 반드시 가장 마지막에 위치해야 함
# 초기값이 지정된 매개변수가 중간에 위치하게 되면 함수사용시 초기값이 지정된 매개변수를 입력하지 않고 
#   사용하였을 경우 그 다음에 있는 매개 변수가 어디에 입력될지 확인이 불가능하여 오류가 발생함
print("# 매개변수 초기값 지정하기")
def say_myself(name, old = 25, man=True):
    print("나의 이름은 {0}입니다.".format(name))
    print("나의 나이는 {0}살입니다.".format(old))
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용")
print()
say_myself("박응선", 27, False)

print()
def say_myself1(name, old = 25, man = True):
    print("나의 이름은 {0}입니다.".format(name))
    print("나의 나이는 {0}살입니다.".format(old))
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself1("최수열", True)

print()
# 기본적으로 변수는 변수가 선언된 함수 내부에서만 메모리에 살아있음
# 함수 외부에 선언된 변수와 함수 내부에 선언된 변수의 이름이 동일한 경우 함수 내부에서는 함수 내부에 선언된 변수만 사용됨
# 함수 내부와 외부에 동일한 이름을 사용한 변수가 있을 경우 함수 외부의 변수를 사용하려면 global 키워드를 사용함(자바의 this와 비슷)
print("# 변수의 사용 범위")

a = 1  # 함수 외부에서 선언된 변수
def vartest(a):
    a = a + 1  # 함수 내부에서 선언된 변수
    print("함수 내부에서 선언된 변수 a : {0}".format(a))

vartest(a)
print("함수 외부에서 선언된 변수 a : {0}".format(a))

print()
b = 10
def vartest2():
    global b
    b = b + 1
    print("global 키워드를 사용한 변수 b : {0}".format(b))

vartest2()
print("함수 외부의 변수 b : {0}".format(b))