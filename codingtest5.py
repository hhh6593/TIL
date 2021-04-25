#하샤드 수
x=10
x=str(x)
y=0
answer=True
for i in x:
    i=int(i)
    y+=i
if int(x)%y==0:
    answer
else:
    False
print(answer)

#문자열 내 맘대로 정렬하기
strings=["sun", "bed", "car"]
n=1
sorted(sorted(strings), key=lambda x:x[n])
