import glob

result = open("result","w",encoding="utf8")
score_name=[]
score_value=[]
for score in glob.glob('*.txt'):
    score_file = open(score,"r",encoding="utf8")
    list = score_file.read().replace('\n',' ').split(' ') # txt의 숫자, 문자 분리
    for i in range(len(list)):
        if i%2 ==0:
            score_name.append(list[i])
        else:
            score_value.append(int(list[i]))
score_dict = dict(zip(score_name,score_value)) #텍스트를 딕셔너리로 최종변환

sorted_dict_key = sorted(score_dict.items()) #딕셔너리 정렬
average_value = sum(score_value) / len(score_value) #평균계산

for name, score in sorted_dict_key:
    print("{0}: {1}".format(name, score),file=result)
print("Average Score: {0:.1f}".format(average_value),file=result) #최종 출력형식을 result.txt에 저장

score_file.close()
result.close()    