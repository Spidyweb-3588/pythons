import random
import time

result=[]
bonus=[]

while len(result) < 6:
    num = random.randint(1, 45) #1부터 45까지 난수 발생
    if num not in result:
        result.append(num)

bonusnum = random.randint(1, 45) #1부터 45까지 난수 발생
if bonusnum not in result:
    bonus.append(bonusnum)

print("####################로또번호생성기시작###################")
for i in range(1,6):
    print(i)
    time.sleep(1)

print(result)
print("보너스번호")
print(bonus)