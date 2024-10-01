from random import *

person_ID="010983-3774936"
last_number=person_ID[12:14]
A=4-int(person_ID[7])
random_number=randint(100,999)      

print("password is %s%d%d"%(last_number,A,random_number))