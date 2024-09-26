
#random 함수 호출
from random import *

#input을 통해 주민번호 받음
주민번호=str(input("주민번호를 입력해주세요"))

#변수 설정
A=주민번호[12:14]
B=4-int(주민번호[7])
C=str(randint(100,999))


print("암호는%s%s%s입니다."%(A,B,C))





















