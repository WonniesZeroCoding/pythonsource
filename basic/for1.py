# for문
# for 변수 in 범위:
# range()는 for문에 많이 사용됨

# range(시작 값, 마지막 범위, 증감)
# print(range(5)) # range(0, 5) range(5) 시작값은 0 이며 끝의 5는 포함X
# print(list(range(5))) # list 함수 list(range()) 범위range에 해당하는 걸 list로 보여줌
# print(list(range(1,5)))
# print(list(range(0,10,2)))

# print(list(range(50,1,-2)))

# 0~9 출력
for i in range(10):
    print(i,end=" ")

print()

for i in range(1,11): #1부터 10까지
    print(i,end=" ")

print()

#1에서 100까지 출력
for i in range(1,101):
    print(i,end=" ")

print()
#1에서 100까지 홀수만 출력
for i in range(1,101,2):
    print(i,end=" ")

print()    
#1에서 100까지 합계 구하여 출력

sum1 = 0
for i in range(1,101):
    sum1 += i
    print("1~100 합계",sum1)

print()

# 실습 : 사용자에게 숫자를 입력받은 후 1~사용자 입력값까지 합계를 구한 후 출력
# number1 = int(input("숫자를 입력하세요 :"))

# sum2 = 0
# for i in range(1,number1):
#     sum2 += i
#     print("입력값의 합계",sum2)

# print("1 ~ {} 까지 합 : {} ".format(number1, sum(range(1,number1+1))))


#문자열 출력
word = "dreams"
for s in word:
    print(s)

#이중 for문
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# 구구단 2~9단
# 2 * 1 = 2 ~~~~~~~~~~~~~~
# 3 * 1 = 3 ~~~~~~~~~~~~~~~

for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,(i*j)), end="\t")
    print()

# break, continue
i = 1
while i<=10:
    if i == 5:
        break
    print(i, end=" ")
    i + 1

print()
i = 1
while i<=10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

print()
# 실습 : 1 ~ 10까지 출력, i가 5인 경우는 출력하지 않음
# for문 + continue 이용
for i in range(1,11):
    if i == 5:
        continue
    print(i, end=" ")
