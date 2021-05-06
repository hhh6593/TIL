#몫과 나머지
#나의 풀이
a, b = map(int, input().strip().split(' '))
print(a//b, a%b)

#정답 풀이
a = 7
b = 5
print(*divmod(a, b)) #unpacking(*) + divmod를 이용한 풀이

#divmod - 두 숫자를 인자로 받아 a 인자를 b 인자로 나눈 몫과 나머지를 tuple 형식으로 반환.  

#############################################################################################

#n진법으로 표기된 string을 10진법 숫자로 변환하기
#나의 풀이
num, base = map(int, input().strip().split(' '))
num=str(num)[::-1]
answer=0
for i in range(len(num)):
    answer+=int(base)**i*int(num[i])
print(answer)

#정답 풀이
num = '3212'
base = 5
answer = int(num, base)

#int() 함수는 진법 변환을 지원한다.

#############################################################################################

#문자열 정렬하기
#나의 풀이
s, n = input().strip().split(' ')
n = int(n)
a = int((n-len(s))/2)
def fnc(s):
    print(s)
    print(' '*a+s)
    print(' '*(a*2)+s)
fnc(s)

#정답 풀이
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

#'가나다라               ' 좌측정렬
#'               가나다라' 우측 정렬
#'       가나다라        ' 가운데 정렬

#############################################################################################

#알파벳 출력하기
#나의 풀이
num = int(input().strip())
a='abcdefghijklmnopqrstuvwxyz'
if num == 0:
    print(a)
else:
    print(a.upper())

#정답 풀이
import string 

#string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
#string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
#string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#string.digits # 숫자 0123456789

#############################################################################################

#2차원 리스트 뒤집기
#나의 풀이
def solution(mylist):   
    return list(map(list, zip(*mylist)))
#mylist를 unpacking한 후 각 리스트의 같은 인덱스 번호끼리 map으로 한번에 append
#ex) mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   (*mylist) = [1,2,3]
#								[4,5,6]
#               [7,8,9]
#   list([1,4,7],[2,5,8],[3,6,9])
#   [[1,4,7],[2,5,8],[3,6,9]]

#############################################################################################

#i번째 원소와 i+1번째 원소
#나의 풀이
def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        try:
            answer.append(abs(mylist[i]-mylist[i+1]))
        except:
            break
    return answer

#정답 풀이
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))

#############################################################################################

#모든 멤버의 type 변환하기
#나의 풀이
def solution(mylist):
	    return list(map(int,mylist))

#############################################################################################

#map 함수 응용하기 - len값을 반환하는 리스트 생성
#나의 풀이
def solution(mylist):
		answer = list(map(len, mylist))
		return answer

#############################################################################################
    
#sequence 멤버를 하나로 이어붙이기
#나의 풀이
def solution(mylist):
    return ''.join(mylist)

#############################################################################################

#삼각형 별찍기
#나의 풀이
n = int(input().strip())
for i in range(1,n+1):
    print('*'*i)

#############################################################################################

#곱집합(Cartesian product) 구하기 - product
#나의 풀이
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))

#############################################################################################

#2차원 리스트를 1차원 리스트로 만들기
#나의 풀이
def solution(mylist):
    from functools import reduce
    return reduce(lambda x,y:x+y,mylist)

#정답 풀이
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용 (리스트 길이가 같은 경우에만 가능)
import numpy as np
np.array(my_list).flatten().tolist()

#############################################################################################

#순열과 조합
import itertools
mylist = [2,1]
sorted(list(map(list, itertools.permutations(mylist)))) #itertools.permutations를 이용해 순열 조합 정렬

#############################################################################################