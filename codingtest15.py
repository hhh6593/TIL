skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
answer=[]
flag=[]
def solution(skill, skill_trees):
    answer=0
    for i in skill_trees:
        skill_li=list(skill)             #스킬 규칙 순서에 맞게 스킬트리가 짜여있는지 인덱스 값별로 비교하기 위해서 리스트 변환
        for j in i:                      #스킬의 순서별로 각 스킬트리에 비교하기 위해 반복문 적용
            if j in skill:               #스킬의 원소가 스킬 안에 있을 경우
                if j != skill_li.pop(0): #스킬의 원소가 각 스킬트리의 제거하는 첫번째 값과 맞지 않을시 break 
                    break                #pop는 삭제 후 값을 취득하기 때문에 del과 다르게 비교가 가능
        else:                            #break로 끊기지 않고 끝까지 반복문을 수행하면 else문 실행
            answer+=1                    #문제가 없으므로 인식하고 answer+=1
    return answer
    
solution(skill, skill_trees)

#