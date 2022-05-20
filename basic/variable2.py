# 문자형 타입
# 자바를 다루든, 파이썬을 다루든 문자형을 잘 쓰는(표현하는) 것이 중요함

# 문자형 - "", ''
str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """
Life is too short, You need Python
"""
str4 = '''
Life is too short, You need Python
'''
str5 = "Python's favorite food"

print(str1)
print(str2)
print(str3)
print(str4)

# + : 문자열 연결
head = "Python"
tail = " is fun"
print(head+tail)

# * 곱하기 기호 : 반복 --> PythonPython
a = "Python"
print(a * 2)

print("*"*50)
print("My Program")
print("*"*50)

# 문자열 인덱싱 <-------- ★ 아주 중요, : 왼쪽을 기준으로 0
str1 = "Life is too short"
print("str1[3]", str1[3]) # e
#오른쪽을 기준으로 -1
print("str1[-3]", str1[-3]) # o
print()
#문자열 인덱싱의 '범위 지정'
#마지막 숫자 범위는 포함 안함
print("str1[0:4]",str1[0:4])
print("str1[4:8]",str1[4:8])
print("str1[9:]",str1[9:])
print("str1[:17]",str1[:17])
print("str1[0:-4]",str1[0:-4])

# 실습
str2 = "20220520Sunny"
#date 변수에 날짜만 담기
date = str2[0:8]
#weather 변수에 날씨만 담기
weather = str2[8:]

print(date)
print(weather)

#date 변수에 있는 값을 2022-05-20 출력
year = date[0:4]
month = date[4:6]
day = date[6:]
print(year,month,day,sep="-") #sep == separator
#date, weather 출력 2022-05-20 sunny 출력
print(year,month,day,sep="-",end=" ")
print(weather) 

#문자열 관련 함수들
#len() == length 문자열 길이
print("문자열 길이",len(str1))
#count() : 문자열에 포함된 특정 문자의 수
print("문자열에 포함된 특정 문자의 수", str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : %d" % str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : {}".format(str1.count('t')))

#find() : 특정 문자가 시작되는 첫번째 위치 반환
#find() : i를 찾게 되면 0을 기준으로 찾은 위치 -- 2번째라면 1 , 찾았는데 없다면 -1
#find('찾을문자',시작위치)
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("i"))
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("k"))
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("i",4))

#index() : 찾는 문자열이 없다면 에러가 발생함 find() 와는 다름
print("특정 문자가 시작되는 첫번째 위치 반환", str1.index("i"))
# print("특정 문자가 시작되는 첫번째 위치 반환", str1.index("k")) # 에러발생 : ValueError : substring not found
print()
#startswith() : boolean타입으로 돌아오고, 대소문자 구별함 

print(str1.startswith("L")) # True
print(str1.startswith("l")) # False

# endswith() : boolean타입으로 돌아오고, 대소문자 구별함 
print(str1.endswith("t")) # True
print(str1.endswith("T")) # False
print()

# join() : 삽입
a = ","
print(a.join("abcde"))
print()
# upper / lower : 대소문자 변경 (자바의 uppercase, lowercase)
a = "abcde"
print("소문자를 대문자로 변경", a.upper())
a = "ABCDE"
print("대문자를 소문자로 변경", a.lower())

#swapcase() : 대문자를 상호 변환 (소문자는 대문자로.. 대문자는 소문자로)
a = "Python is Easy"
print(a.swapcase())
# title() : 첫글자만 대문자
print("python Is Easy".title())

print("abc" == "ABC")

print()

# 공백제거 : strip(), lstrip(), rstrip()
a = "   h1   "
print(a.lstrip()) #왼쪽 공백제거 left strip
print(a.strip()) # 양쪽 공백제거
print(a.rstrip()) # 오른쪽 공백 제거
print()
# replace() : 문자열 바꾸기
print(str1.replace("Life","Your leg"))
print()
# split() : 문자열 나누기(default 값은 공백)
print(str1.split()) # ['Life', 'is', 'too', 'short] --> 리스트 구조로 리턴됨
a = "a:b:c:d"
print(a.split(":")) # : 을 기준으로 나눠줘 -> ['a', 'b', 'c', 'd']

# splitlines() : 줄바꿈을 기준으로 나누기
a = "하나\n둘\n셋"
print(a.splitlines()) # ['하나', '둘', '셋'] :: 줄바꿈이 일어났다면 일어난 줄바꿈을 기준으로 나눠줌

# 문자열 구성 파악
print("1234".isdigit())
print('abcd'.isalpha())
print('abc123'.isalnum())
print("abcd".islower())
print("ABCD".isupper())

# 실습 : 암호 생성
# http://naver.com <-- 원본 문자열
# 규칙 1 : http:// 부분은 제외 ==> naver.com
# 규칙 2 : 처음 만나는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 문자 갯수 + ! 로 구성
# 결과 : nav51!
url = "http://naver.com"
url = url.replace("http://","")
url = url[:url.find(".")]
e_cnt = url.count("e")

 # 문자 + 숫자 : 연결 되지 않음 (에러 나옴 - TypeError: can only concatenate str (not "int") to str)
 # 문자 + str(숫자) : 연결
password = url[:3]+str(len(url))+str(e_cnt)+"!"
print(password)

