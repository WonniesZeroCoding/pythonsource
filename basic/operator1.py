# 연산자

#산술 연산자 : +,-,*,/(실수형태 나누기),//(정수형태 나누기),%(나머지연산자), **(제곱)

a,b = 5,3
print(a+b, a-b,a*b,a/b,a//b,a%b,a**b)

print()
s1,s2,s3 = "100", "100.123", "99999999"
print(s1+s2+s3) # + : 문자열 연결 => 100100.123999999999
#문자열이아니라 진짜로 연산하고 싶으면 문자열-> 실수형 
print(float(s1)+float(s2)+float(s3))
print(int(s1)+1) # 하나는 str, 하나는 int -> 타입 에러 TypeError : can only concatenate str (not "int") to str

# 복합 대입 연산자 +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5
print("a",a)
a == 5
print("a",a)
a *=5
print("a",a)
a /=5
print("a",a)
a //=5
print("a",a)
a %=5
print("a",a)
a **=5
print("a",a)

#실습 : 777,777 원
#화폐 교환 : 5만원 권, 1만원권, 5천원 권, 1천원 권으로 몇장 나오나
# 50000만원으로 먼저 바꿔주고 안되는건 1만원 --> 5 -> 1
x = 777777

x50000 = x // 50000
x %= 50000

x10000 = x // 10000
x %= 10000

x5000 = x // 5000
x %= 5000

x1000 = x // 1000
x %= 1000

print("50,000원 : %d 장" % x50000)
print("10,000원 : %d 장" % x10000)
print("5,000원 : %d 장" % x5000)
print("1,000원 : %d 장" % x1000)
print("나머지 돈 : %d " % x)

#관계 연산자 : ==, !=, >, <, <=, >=
a,b = 10, 0
print(a == b, a != b, a>b, a<b, a>=b, a<=b)

#논리 연산자 : and, or, not
print(100 > 60 and 60 > 15)
# print(100 > 60 && 60 > 15) 자바랑 다른점
print(100 > 60 or 60 > 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!True) 자바랑 다른 점

#비트 연산자 :
print(10 & 7)
print(10 | 7)
print((100 > 60) & (60 > 15))




