#3진법 뒤집기
n=125
result=''
while n>=1:
    if n%3==0:
        result='0'+result
        n=n//3
    elif n%3!=0:
        result=str(n%3)+result
        n=n//3
result
range(len(result))
max(range(len(result)))
answer=[]
for i in range(len(result)):
    if int(result[i])==0:
        answer.append(int(result[i]))
    else:
        answer.append(3**i*int(result[i]))
print(sum(answer))

#두 개 뽑아서 더하기
numbers=[3,4,8,1]
answer=[]
for i in range(len(numbers)):
    j=i+1
    for j in range(len(numbers)):
        if j>i:
            answer.append(numbers[i]+numbers[j])
answer=sorted(set(answer))
answer

#내적
a,b=[1,2,3,4],[-3,-1,0,2]
answer=[]
for i,j in zip(a,b):
    answer.append(i*j)
print(sum(answer))

#핸드폰 번호 마스킹
phone_number="01033334444"
print(phone_number[-4:])
num=len(phone_number)

#소수찾기
n=10
answer=[]
list=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%j==0:
            list.append(j)
    if len(list)==2:
        answer.append(i)
        list=[]
    else:
        list=[]
answer




    
