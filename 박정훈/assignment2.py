student = { 70 : "성균관대", 80 : "경기대", 95 : "아주대", 75 : "경희대", 85 : "수원대"}

for i in student.keys():
    print(i,end=" ")

print(" ")

for j in sorted(student.keys()):
    print(j,end=" ")

print(" ")

b = sorted(student)
c = list(b)
c.reverse()

d = print("이번 시험 1등은 " + student[c[0]] + "입니다.")