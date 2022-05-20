# 입력 : input() -- 자바에서 Scanner로 값 입력하는 것과 동일

# msg = input()
# print(msg)

# msg = input("이름 입력 : ")
# print(msg)

# num1 = input("Num1 : ") #str 타입으로 입력
# num2 = input("Num2 : ") 
# print(num1 + num2) # str 타입에서 +는 문자열 연결 4555

# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# print(num1 + num2)

# 실습
# 년/월/일 형태로 입력 받은 후 10년 후 날짜를 출력하기
# 2022/05/20 => 2032년 05월 20일
date1 = input("날짜입력(년/월/일) ")
pos = date1.find("/")
year = int(date1[:pos]) + 10
print("입력한 날짜의 10년 후는 ? %s" % (str(year)+"년 "+date1[5:7]+"월 "+date1[8:]+"일") )