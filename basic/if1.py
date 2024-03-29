# 파이썬 {} 사용하지 않음 / 들여쓰기를 사용함
# if 
# if True:
#     print("True") # <-- enter써서 들여쓰기가 자동으로 들어감, 변동시키면 X. 자동으로 생성되는 것만

a = 200
# if a < 200:
#     print("a는 100보다 작다")
# print("조건문에서 들여쓰기는 중요함") 

# a는 100과 200사이에 있다 
# if a >= 100 and a <= 200:
#     print("a는 100과 200사이에 있다")   

# if 100 <= a <= 200:
#     print("a는 100과 200사이에 있다") 

# 실습
# a, b, c = 12,6,18

# if문을 사용해 가장 큰 수 출력하기
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c

# print("제일 큰 수",max)

# if~else

if True:
    print("True")
else:
    print("False")

a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 작다")

print()

score, grade = 90,"A"
if score >= 90 and grade == "A": #if문에서 관계연산자를 많이쓴다
    print("합격")
else:
    print("불합격")


# 실습 - 숫자를 입력받아 짝수 / 홀수 출력
# num1 = int(input("숫자입력 : "))

# if num1 % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
print()
import datetime

now = datetime.datetime.now()
print(now) #2022-05-20 15:11:39.601818
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

if now.hour < 12:
    print("오전")
else:
    print("오후")

print("오전" if now.hour < 12 else "오후")

# 삼항 연산자
str = "안녕하세요 " if True else "반갑습니다."
print(str)

#중첩 if
a = 75
if a > 50:
    if a < 100:
        print("a는 50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")

#다중 if : if ~ elif ~ else

num = 90
if num >= 90:
    print("등급 A",num)
elif num >= 80:
    print("등급 B", num)
elif num >= 70:
    print("등급 C", num)
elif num >= 60:
    print("등급 D", num)
else:
    print("등급 E", num)

print()
age, height = 27, 180

if age >= 20:
    if height >= 170:
        print('A 지망 가능')
    elif height >=160:
        print('B 지망 가능')
    else:
        print('지원 불가')
else:
    print("20세 이상 지원 가능")

print()
#실습
# 사용자에게 점수를 입력 받고 학점 출력
# > 80 (초과) A학점 , > 60 B학점, > 40 C학점, > 20 D학점, 아니면 E학점

score = int(input("점수 입력 : "))
if score > 80:
    print(score, "A 학점")
elif score > 60:
    print(score, "B 학점")
elif score > 40:
    print(score, "C 학점")
elif score > 20:
    print(score, "D 학점")
else:
    print("E 학점")

print()

# 사칙계산기
# 사용자에게 숫자 2개와 연산자(+, -, *, /, %, //, **) 입력 받은 후 연산을 한 후 결과 출력
num1 = int(input("input num1 : "))
op = input("+, -, *, %, //, ** 중 하나 입력 :")
num2 = int(input("input num2 : "))

result = 0
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "%":
    result = num1 % num2 
elif op == "//":
    result = num1 // num2
elif op == "**":
    result = num1 ** num2
else:
    print("연산자 확인")

print("{} {} {} = {}".format(num1,op,num2,result))           