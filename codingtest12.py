# #직사각형 별찍기
# a, b = map(int, input().strip().split(' '))
# print(('*'*a + '\n')*b)

# #2016년
# def solution(a, b):
#     import datetime as dt
#     answer=['MON','TUE','WED','THU','FRI','SAT','SUN']
#     # wday = dt.date(2016,a,b).weekday()
#     return answer[dt.date(2016, a, b).weekday()]

# solution(1,1)

# #이상한 문자 만들기
# s="try hello world"
# split_s=s.split(" ") #하나 이상의 공백일 경우도 있어 ' '라는 조건을 추가로 넣어주어야 한다.
# split_s
# answer=''
# for i in split_s:
#     for j in range(len(i)):
#         if j==0:
#             answer+=i[j].upper()
#         elif j%2==0:
#             answer+=i[j].upper()
#         else:
#             answer+=i[j].lower()
#     answer+=' '
# answer[:-1]

#폰켓몬
nums=[3,3,3,2,2,4]
cho=len(nums)/2
answer=0
if len(set(nums))>cho:
    answer=len(set(nums))-(len(set(nums))-cho)
else:
    answer=len(set(nums))
answer
