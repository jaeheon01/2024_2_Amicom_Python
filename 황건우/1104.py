# 모듈 불러오기
import glob # glob 모듈을 불러온다.

#파일 불러오기 및 dictionary 선언
text_files=glob.glob("scores*.txt") #glob 모듈을 통해, scores로 시작하는 모든 txt파일을 불러와서 리스트 형태로 text_files에 저장
student_and_value={} # key:value 형태로 scores*.txt에 저장된 값들을 사용할 것이기에, dictionary를 이용한다.

#파일 불러오기, student_and_value에 저장 및 정렬
for file in text_files: # text_files에 있는 파일에 대해 (이 경우 scores1.txt와 scores2.txt, 두 번 반복문이 실행된다.)
    with open(file, "r", encoding="utf8") as text_file: # with문을 사용해, 추가적인 열기 및 닫기를 하지 않고, 일회성으로 사용한다.
        # text_files에 있는 file 2개에 대해서, 각각을 text_file로, 반복문을 통해 열어준다.
        for line in text_file: # 한번 선택한 text_file에 대해, 해당 text_file 내의 각 줄에 대해 반복문을 걸어준다.
            name,score=line.strip().split() # 공백으로 구분된 이름:점수 값을 key:value로 설정한다.
            student_and_value[name]=int(score) # student_and_value dictionary안에 key:value로 받아준다.
sorted_keys=sorted(student_and_value.keys()) # 그리고 이것들을 이름순으로 정렬해준다.

#평균 점수 계산
average=0 # 평균 점수를 계산해야하기에, average의 초기값을 0으로 설정해준다.
for keys in sorted_keys: # sorted_keys에 있는 key들을 사용해 value를 불러올 것이기에, sorted_keys에 있는 key들에 대해 반복문을 걸어준다.
    average+=student_and_value[keys] # 모든 value값을 더하고,
average=average/len(sorted_keys) # sorted_keys에 있는 key들의 개수만큼 나눠 평균값을 구한다.

#앞선 데이터를 이용해 파일 출력
with open("result.txt","w",encoding="utf8") as answer: # 정렬된 이름과 점수 및 평균 점수를 작성할 파일, with를 통해 answer라는 이름으로 연다.
    for key in sorted_keys: # sorted_keys에 있는 key들에 대해.
        answer.write(key+" : "+str(student_and_value[key])+"\n") #각 줄별로 이름 : 점수 형태로 작성한다. 이때 int형 data type은 +를 통해 연경할 수 없으므로
        # str을 통해 문자열로 바꿔주고, 줄바꿈을 위해 "\n"을 이용한다.
    answer.write("Average score : {}".format(average)) # 마지막 줄에는 계산한 average값을 format을 통해 불러온다.