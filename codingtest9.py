#비밀지도 2018 KAKAO BLIND RECRUITMENT
n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
def solution(n, arr1, arr2):
    pw1=[]
    pw2=[]
    y=0
    answer=[]
    for i in range(len(arr1)):
        a1=''
        while arr1[i]>=1:
            if arr1[i]%2==0:
                a1='0'+a1
                arr1[i]=arr1[i]//2
            else:
                a1='1'+a1
                arr1[i]=arr1[i]//2
        if len(a1)<n:
            a1='0'*(n-len(a1))+a1
        pw1.append(a1)
    for i in range(len(arr2)):
        a2=''
        while arr2[i]>=1:
            if arr2[i]%2==0:
                a2='0'+a2
                arr2[i]=arr2[i]//2
            else:
                a2='1'+a2
                arr2[i]=arr2[i]//2
        if len(a2)<n:
            a2='0'*(n-len(a2))+a2
        pw2.append(a2)
    while len(answer)<n:
        x=0
        pk=''
        for x in range(n):
            if pw1[y][x]=='1' or pw2[y][x]=='1':
                pk=pk+'#'
                x+=1    
            elif pw1[y][x]=='0' and pw2[y][x]=='0':
                pk=pk+' '
                x+=1
        if len(pk)==n:
            answer.append(pk)
            y+=1
            continue
    return answer

solution(n,arr1,arr2)

#신규 아이디 추천
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
new_id=	"abcdefghijklmn.p"
len(new_id)
new_id[:15]
answer=''
new_id=new_id.lower()
for i in new_id:
    if(i.isalpha()==True or i.isdigit()==True or i in ['-','_','.']):
        answer=answer+str(i)
while '..' in answer:
    if '..' in answer:
        answer=answer.replace('..','.')
answer=answer.strip('.')
if len(answer)==0:
    answer+='a'
if len(answer)>=16:
    answer=answer[:15]
answer=answer.strip('.')
if len(answer)<=2:
    while len(answer)<3:
        sev=answer[::-1]
        answer+=sev[0]
print(answer)