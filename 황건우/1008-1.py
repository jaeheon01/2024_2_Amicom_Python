#과제 1

import random # random 모듈 호출
customers={} # n번째 손님과 그 손님의 시간을 dictionary의 key:value 형태로 저장
for i in range(1,51): # for문을 1부터 50까지 50번 돌리자
    riding_time=random.randint(5,51) #탑승 시간은 5분 이상 50분 이하.
    customers[i]=riding_time # n번째 손님의 key를 반복문의 번호를 통해 지정, random모듈을 통해 만든 탑승 시간을 value로 지정
    print("{}번째 손님 (소요시간:{}분)".format(i,customers[i])) #format을 통해, dictonary의 key와 value를 돌린다. list로 하면 두개로 해야하는데, 이렇게 하면 하나만으로 가능하다.
for i in list(customers.keys()): #조건을 만족하는 손님을 찾는 반복문. customers dictionary의 key를 리스트로 바꿔 1부터 50까지의 숫자를 저장한다.
    if customers[i]>=16 or customers[i]<=4: # 5분 미만, 15분 초과라면...
        customers.pop(i) # dictonary에서 제외한다.
print("총",len(customers),"명의 손님") # dictionary에 저장된 손님의 수만 세준다.