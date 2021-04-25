#모의고사
st1=[1, 2, 3, 4, 5]*10000
st2=[2, 1, 2, 3, 2, 4, 2, 5]*10000
st3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*10000
answers=[1,3,2,4,2]
list=[]
check1,check2,check3=0,0,0
result=[]
for i in range(len(answers)):
    if answers[i]==st1[i]:
        check1+=1
    if answers[i]==st2[i]:
        check2+=1
    if answers[i]==st3[i]:
        check3+=1
list.append(check1)
list.append(check2)
list.append(check3)
if max(list)==check1:
    result.append(1)
if max(list)==check2:
    result.append(2)
if max(list)==check3:
    result.append(3)
result

#소수 만들기
nums=[1,2,3,4]
def checking(x):
    list=[]
    for i in range(1,x+1):
        if x%i==0:
            list.append(i)
    if len(list)==2:
        return True
    else:
        return False
from itertools import combinations as cb
result=0
a=cb(nums, 3)
for i in a:
    x=sum(i)
    if checking(x)==True:
        result+=1
    else:
        pass
