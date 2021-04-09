#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 
#다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
#단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
s="Pyy"
s=s.upper()
p=s.count('P')
y=s.count('Y')
if p==y:
    answer=True
else:
    answer=False
print(answer)

#함수 solution은 정수 n을 매개변수로 입력받습니다. 
#n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
#예를들어 n이 118372면 873211을 리턴하면 됩니다.

n=118372
n=str(n)
list=[]
answer=0
for i in range(len(n)):
    list.append(n[i])
list=sorted(list)
print(int("".join(list)))