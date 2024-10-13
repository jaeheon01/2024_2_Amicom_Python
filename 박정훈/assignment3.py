import random as r
i = 0
j = 0
while i != 50:
    t = r.randint(5,50)
    i = i + 1
    print("{0}번째 손님 (소요시간 : {1}분)".format(i,t))
    if 5 <= t <= 15:
        j = j + 1
print("총 탑승 승객 : {0}분".format(j))