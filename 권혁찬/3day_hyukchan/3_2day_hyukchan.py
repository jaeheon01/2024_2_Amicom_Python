import random as rm
import string

def generate_password(length, upper, lower, num, spec):

    upper_set = string.ascii_uppercase
    lower_set = string.ascii_lowercase
    digits_set = string.digits
    special_set = string.punctuation

    mix_set = upper_set+lower_set+digits_set+special_set

    pw = []

    if upper == "y":
        pw.append(rm.choice(upper_set))

    if lower == "y":
        pw.append(rm.choice(lower_set))

    if num == "y":
        pw.append(rm.choice(digits_set))

    if spec == "y":
        pw.append(rm.choice(special_set))


    if length < len(pw):
        return '오류'
    
    pw += [rm.choice(mix_set) for _ in range(length - len(pw))]


    rm.shuffle(pw)

    return ''.join(pw)


length = int(input("암호의 길이를 입력하세요:"))

upper = input("대문자를 포함할까요? (y/n):")
lower = input("소문자를 포함할까요? (y/n):")
num = input("숫자를 포함할까요? (y/n):")
spec = input("특수문자를 포함할까요? (y/n):")

password = generate_password(length, upper, lower, num, spec)

print(password)