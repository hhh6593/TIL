#시저암호
s="a B z"
n=4
list=[]
alpha_low='abcdefghijklmnopqrstuvwxyz'*100
alpha_upp=alpha_low.upper()
for i in s:
    if i in alpha_upp:
        a=alpha_upp.index(i)
        list.append(alpha_upp[a+n])
    elif i in alpha_low:
        a=alpha_low.index(i)
        list.append(alpha_low[a+n])
    else:
        list.append(' ')
answer=''.join(list)
answer

#행렬의 덧셈
arr1=[[1],[2]]
arr2=[[3],[4]]
answer = []
for i,j in zip(arr1,arr2):
    a=[]
    for k in range(len(arr1[0])):
        try:
            a.append(i[k]+j[k])
        except:
            a.append(i[k-1]+j[-1])
    answer.append(a)


        
