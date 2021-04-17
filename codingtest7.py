#예산 summer/winter coding 2018
d=[1,3,2,5,4]
budget=9
answer=[]
d=sorted(d)
a=budget
cnt=0
i=0
while len(answer)<len(d):
    try:
        if d[i]<=budget:
            budget-=d[i]
            i+=1
            cnt+=1
        elif d.sum():
            print('error') #고의적으로 에러를 발생시켜 except로 넘어가게 설정
    except:
        i=0
        d.append(d[0])
        del d[0]
        budget=a
        answer.append(cnt)
        cnt=0
        continue
print(max(answer))

#행렬의 덧셈
arr1=[[1,2],[2,3],[3,4],[1,2],[2,3],[3,4],[1,2],[2,3],[3,4]]
arr2=[[3,4],[5,6],[7,8],[3,4],[5,6],[7,8],[3,4],[5,6],[7,8]]
def solution(arr1, arr2):
    answer = []
    j=0
    if len(arr1[0])>1:
        try:    
            for i in range(len(arr1)):
                j+=1
                for x,y in zip(arr1, arr2):
                    answer.append([x[i]+y[i],x[j]+y[j]])
        except:
            pass
    else:
        try:
            for i in range(len(arr1)):
                for x,y in zip(arr1, arr2):
                    answer.append([x[i]+y[i]])
        except:
            pass
    return answer

#정수 제곱근 판별
import numpy as np
n=3
if n%np.sqrt(n)==0:
    n=np.sqrt(n)+1
    answer=int(n*n)
else:
    answer=-1
print(answer)
        
#음양 더하기
absolutes=[4,7,12]
signs=[True,False,True]
list=[]
for i,j in zip(absolutes, signs):
    if j == True:
        i=i
        list.append(i)
    else:
        i=-i
        list.append(i)
answer=sum(list)
print(answer)

#자릿수 더하기
N=123
sn=str(N)
list=[]
for i in sn:
    list.append(int(i))
sum(list)
sn.split()

#수박수박수박수박수박수?
n=3
watermelon='수박'*1000
answer=watermelon[:n]
answer

#문자열 내림차순으로 배치하기
s="Zbcdefg"
ss=sorted(s,reverse=True)
answer=''.join(ss)
answer

#서울에서 김서방 찾기
seoul=["Jane", "Kim"]
answer=seoul.index('Kim')
print('김서방은'+' '+str(answer)+'에 있다.')

#약수의 합
n=12
answer=[]
for i in range(1,n+1):
    if n%i==0:
        answer.append(i)
print(sum(answer))

#문자열 다루기 기본
s="a234"
def solution(s):
    answer=True
    if len(s)==4 or len(s)==6: #문자열의 길이가 4 또는 6이어야만 함.
        for i in range(len(s)):
            if not s[i].isdigit():
                answer=False
                break
    else:
        answer=False
    return answer
