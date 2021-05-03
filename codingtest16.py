#크레인 인형뽑기
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
answer=[]
cnt=0
for i in moves:
    i-=1
    for j in board:
        if j[i]==0:
            continue
        else:
            answer.append(j[i])
            j[i]=0
            break
    if len(answer)>1:
        for k in range(len(answer)):
            if answer[k]==answer[k-1] and k>0:
                try:
                    cnt+=2
                    answer.pop()
                    answer.pop()
                except:
                    cnt+2

#체육복
def solution(n, lost, reserve):
    answer=[]
    for i in range(1,n+1):
        if (i in lost and i in reserve):
            lost.remove(i)
            reserve.remove(i)
    for i in range(1,n+1):
        if i in lost:
            if i-1 in reserve:  
                answer.append(i)
                del lost[lost.index(i)]
                del reserve[reserve.index(i-1)]
            elif i+1 in reserve:
                answer.append(i)
                del lost[lost.index(i)]
                del reserve[reserve.index(i+1)]
        else:
            answer.append(i)
    return len(answer) 