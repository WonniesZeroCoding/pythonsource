# while : tab 같은 블럭임을 표시해야 함

# 1 ~ 10 출력
i = 1
while i < 11: # 조건 설정
    print(i) # 옆으로 출력하길 원한다면 end = " "
    i = i + 1 # 증감 부분이 반드시 있어야함 (자바 i++)
    
# 1 ~ 100 짝수만 출력
i = 2
while i < 101:
    print(i, end=" ")
    i += 2

print()
# 1 ~ 100 홀수 출력
i = 1
while i < 101:
    print(i, end=" ")
    i += 2 

print()

# i는 1씩 증가, if문 사용하여 1~100까지의 홀수 출력
i = 1
while i < 101:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1

print()

# 1 ~ 100까지 합계 출력
i, sum1 = 1,0
while i <= 100:
    sum1 += i
    i += 1

print("1~100 합계", sum1)

# sum() 함수
# range(시작 숫자, 끝나는 숫자, 증감값) 함수
print(sum(range(1,100)))

print()
# 구구단 3단, while문 이용해서 출력

# i= 3
# j= 1
 
# while j < 10:
#     print(i*j)
#     j = j+1

i=1
while i < 10:
    print('%d * %d = %d' % (3, i, (3*i)))
    i += 1