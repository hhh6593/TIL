#1번 문제
s="23four5six7"
s=list(s)
answer=[]
for i in range(len(s)):
    try:
        if s[i]+s[i+1] == 'ze':
            answer.append('0')
        elif s[i]+s[i+1] == 'on':
            answer.append('1')
        elif s[i]+s[i+1] == 'tw':
            answer.append('2')
        elif s[i]+s[i+1] == 'th':
            answer.append('3')
        elif s[i]+s[i+1] == 'fo':
            answer.append('4')
        elif s[i]+s[i+1] == 'fi':
            answer.append('5')
        elif s[i]+s[i+1] == 'si':
            answer.append('6')
        elif s[i]+s[i+1] == 'se':
            answer.append('7')
        elif s[i]+s[i+1] == 'ei':
            answer.append('8')
        elif s[i]+s[i+1] == 'ni':
            answer.append('9')
        elif s[i].isdigit() == True:
            answer.append(s[i])
    except:
        if s[i].isdigit() == True:
            answer.append(s[i])
print(int(''.join(answer)))

#1번 문제 다른 방법 시도 - 코드 간소화 시도 중
dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
for i in range(len(s)):
    try:   
        if s[i+1].isnumeric() == True:
            answer.append(dic[''.join(s[:i+1])])
        elif s[i].isnumeric() == True:
            answer.append(int(s[i]))
 
#3번 문제
n=8
k=2
cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
cell = 'O'*n
cell = list(cell)
x = []
i=k
for j in cmd:
    if j[0] == 'D':
        if i+int(j[2]) > n-1:
            i = abs((n-1)-i+int(j[2]))-1
        else:    
            i += int(j[2])
    elif j[0] == 'U':
        if i-int(j[2]) < 0:
            i = (n-1) - (j[2]-i) 
        else:   
            i -= int(j[2])
    elif j[0] == 'C':
        cell[i] = 'X'
        i+=1
        x.insert(0, i-1)
cell
for k in x[:cmd.count('Z')]:
    cell[k] = 'O'
''.join(cell)



