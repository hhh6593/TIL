#가운데 글자 가져오기
def solution(s):
    import numpy as np
    if len(s)%2>0:
        a=int(np.median(range(1,len(s)+1)))
        s=s[a-1]
    if len(s)%2==0:
        b=int(np.median(range(1,len(s)+1)))
        s=s[b-1:b+1]
    return s

s='abcde'

#두 정수의 범위 합 구하기
a,b=3,5
if a==b:
    answer=a
else:
    list=[]
    answer=[]
    list.append(a)
    list.append(b)
    mi=min(list)
    ma=max(list)
    range(mi,ma)
    for i in range(mi,ma+1):
        answer.append(i)
    print(sum(answer))

#자연수 뒤집어 배열로 만들기
from functools import reduce
n=12345
n=str(n)
answer=[]
b=reduce(lambda x,y:y+x,n)
for i in b:
    answer.append(int(i))
answer
