#실패율 2019 KAKAO BLIND RECRUITMENT
N=5 #스테이지 개수
stages=[2, 1, 2, 6, 2, 4, 3, 3] #현재 멈춰있는 스테이지의 번호
stages=sorted(stages)
players=len(stages)
answer=[]
result=[]
for j in range(1,N+1):
    cnt=stages.count(j)
    if players==0:
        loser=0
    else:
        loser=cnt/players
    answer.append(loser)
    players-=cnt
answer=dict(zip(range(1,N+1),answer))
answer=sorted(answer.items(), key=lambda x:x[1], reverse=True) #딕셔너리 value 기준으로 정렬
for i in answer:
    result.append(i[0])
result