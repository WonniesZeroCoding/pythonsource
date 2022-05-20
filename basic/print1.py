# print() 알아보기 - 화면출력
# 옵션 
# - 1) sep : ,로 들어오는 출력문자들의 구분을 어떻게 할 것인가?
# - 2) end : 줄바꿈을 하지 않고 다음 줄과 연결해서 출력


print("Hello Python!!") # 문자열 - 쌍따옴표, 홑따옴표 허용
print('Hello Python!!')
print(100)
print("100")
print("25.3")
print(25)
print()

# type() 함수 : 현재 변수 타입 확인할 때 사용
print(type(100)) # <class 'int' >
print(type("100")) # <class 'str' >
print(type(25.5)) # <class 'float' >
print(type(True)) # <class 'bool' >
print()

print('T','E','S','T') # T E S T <-- 스페이스바가 붙어서 나옴
print('T','E','S','T', sep='') # TEST  sep='' 스페이스바 안하게 가능 
print('2022','05','19',sep='-') # 2022-05-19 sep'-' 문자열 연결가능
print("niceman","naver.com",sep="@") # niceman@naver.com 연결 문자열 지정 가능
print()

print("파이썬 ", end=' ')
print("쉬운 언어 입니다.")