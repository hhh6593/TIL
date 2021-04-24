#나누어 떨어지는 숫자 배열
arr=[2, 36, 1, 3]
divisor=1
answer=[]
for i in arr:
    if i%divisor==0:
        answer.append(i)
    else:
        continue
if answer==[]:
    answer.append(-1)
answer.sort()
print(answer)

#정수 내림차순으로 정렬하기
n=118372
a1=sorted(str(n), reverse=True)
answer=int(''.join(a1))
answer

#콜라츠 추측
num=6
cnt=0
while num > 1:
    if num%2==0:
        num/=2
        cnt+=1
    else:
        num*=3
        cnt+=1
        num+=1
if cnt>500:
    cnt=-1
print(cnt)
