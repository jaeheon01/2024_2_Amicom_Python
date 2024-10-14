import random as rm

passenger= list(range(1,51))
time = [rm.randint(5, 51) for _ in range(50)]
dict = dict(zip(passenger,time))

count = 0

for i in dict.keys():
    if dict[i] >= 5 and dict[i] <= 15:
        count += 1
        print(f"[0] {i}번째 손님 (소요시간 : {dict[i]}분)")
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {dict[i]}분)")

print(f"총 탑승 승객 : {count}분")