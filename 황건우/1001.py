# 성적순으로 줄지어 1등을 뽑으세요. 1줄 : 점수, 2줄 : 정렬된 점수, 3줄 : 이번 시험 1등은 아주대입니다.
student = {90 : "성균관대", 80 : "경기대", 95 : "아주대", 75 : "경희대", 85 : "수원대"}

# key list 정의, dictionary의 내장 함수 통해 key값만을 부른 후 list화 및 출력
key_list=student.keys()
key_list=list(key_list)
print("정렬 전 점수 순서는 {}입니다.".format(key_list))

# sort 통해 key_list 정렬
key_list.sort()
print("정렬 후 점수 순서는 {}입니다.".format(key_list))
print("이번 시험 1등은 {}입니다.".format(student[key_list[len(key_list)-1]]))