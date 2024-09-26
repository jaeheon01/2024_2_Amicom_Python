import random

def generate_password(ssn):
    # 주민등록번호 뒷자리에서 마지막 두 자리를 암호의 첫 번째, 두 번째 숫자로 사용
    first_two = ssn[-2:]
    
    # 주민등록번호 뒷자리 첫 번째 숫자가 3이면 남성(1), 4이면 여성(0)
    # 2로 나눈 나머지 값은 3은 1, 4는 0으로 변환
    gender = str(int(ssn[7]) % 2)
    
    # 100부터 999까지의 숫자 중 무작위로 하나 선택
    random_number = random.randint(100, 999)
    
    # 암호 생성 및 포맷팅
    password = f"{first_two}{gender}{random_number}"
    
    return password

# 사용자로부터 주민등록번호 입력받기
ssn = input("주민등록번호를 입력하세요 (형식: xxxxxx-xxxxxxx): ")

# 암호 생성 및 출력
password = generate_password(ssn)
print(f"생성된 암호: {password}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

