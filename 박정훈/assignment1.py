from random import *

jumin = input("주민번호를 입력하시오: ")

a = int(jumin[12])
b = int(jumin[13])
c = int(jumin[7]) % 2
d = randint(100,999)
e = d + c * 1000 + b * 10000 + a * 100000

print("생성된 암호: {}" .format(e))