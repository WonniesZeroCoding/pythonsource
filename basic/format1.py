# format() 함수 <-- 출력을 할 때 예쁘게 출력하고 싶을 때(줄 맞추기)
# ~~.printf("%d",3) 와 같은 개념
# %c - 문자 하나, %f- 실수, %d - 정수, %s-문자(만능)

# print('%d' % 100)
# print('%5d' % 100) # 5자리 맞춰서 출력
# print('%05d' % 100) 
# print()

# print("%s" % "hi")
# print("%5s" % "hi")
# print()

# print("%8.2f" % 12.21)
# print("%-8.2f" % 12.21)
# print("%-8.2f" % 12.2134567)
print()

print("I eat %d apples" % 3)
print("I eat %s apples" % 3)
number = 4
print("I eat %d apples" % number)
print("I eat", number, "apples")
 # 문자열과 변수가 가지고 있는 변수 값이 출력이 되어야할 때, 사용하면 편함
print()
print("%d : %s" % (1, "홍길동"))
print("%d : %s - %f" % (2, "김성호", 93.2))
print("Test1 : %5d Price : %4.2f" % (776,5634.123))
print()
print("I et %s apples" % 3) 
print("I et %s apples" % 3.156) 
print("I et %s apples" % "3")
print()
print("Error is %d%%" % 98)
 