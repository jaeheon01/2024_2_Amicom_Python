#라이브러리 불러오기 
import random as rm
#입력 받기
a = input("주민번호를 입력해 주세요. xxxxxx-xxxxxxx :")


#슬라이싱
x = a[12:]

#인덱스
y = 4 - int(a[7])

#라이브러리 사용
z = rm.randrange(100,999)


#출력하기 format사용
print("{}{}{}".format(x,y,z))
#또는
print(f"{x}{y}{z}")
#또는
print('%s%s%s'%(x,y,z))