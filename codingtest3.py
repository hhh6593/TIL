numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand='right'
answer=[]
ps={1:(1,1),2:(1,2),3:(1,3),
    4:(2,1),5:(2,2),6:(2,3),
    7:(3,1),8:(3,2),9:(3,3),
    '*':(4,1),0:(4,2),'#':(4,3)}
left='*'
right='#'
for i in numbers:
    if i in [1,4,7]:
        left=i
        answer.append('L')
    if i in [3,6,9]:
        right=i
        answer.append('R')
    if i in [2,5,8,0]:
            goal=ps[i]
            left_ps=ps[left]
            right_ps=ps[right]
            left_dis=abs(left_ps[0]-goal[0])+abs(left_ps[1]-goal[1])
            right_dis=abs(right_ps[0]-goal[0])+abs(right_ps[1]-goal[1]) 
            if left_dis<right_dis:
                left=i
                answer.append('L')
            if left_dis>right_dis:
                right=i
                answer.append('R')
            if left_dis==right_dis:
                if hand=='left':
                    left=i
                    answer.append('L')
                else:
                    right=i
                    answer.append('R')        
a=''.join(answer)
a
#기댓값 "LRLLLRLLRRL"