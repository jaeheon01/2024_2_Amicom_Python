#10.1 과제. 

student = {
90 : "성균관대",
80 : "경기대",
95 : "아주대",
75 : "경희대",
85 : "수원대"
}

# print(student.keys()) 출력값이 'dict_keys'의 타입으로 나오기 때문에 적절하지 않음.
# 타입 출력 코드 print(type(student.keys()))

for i in student.keys():
    print(i, end=" ")
# int타입의 정렬로 출력

print()
#줄바꿈


for i in sorted(student.keys()):
    print(i, end=" ")
#점수 오름차순 정렬 출력

print()
#줄바꿈


a = student.get(max(student.keys()))
#점수 1등의 키값을 max함수를 이용해서 찾고 그 키값에 대응되는 벨류값을 변수에 저장. 

print(f"이번 시험 1등은 {a}입니다.")
#결과 출력
