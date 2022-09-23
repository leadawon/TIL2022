'''
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
 

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
 

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
 

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

입력
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX	 
sample_input.txt
출력
#1 1
#2 4
#3 11	 
sample_output.txt
'''
import sys
from collections import deque
sys.stdin = open("testcase.txt","r")

T=int(input())
ans=[]
dq = deque()
for i in range(T):
    str = input()
    if len(str)==1:
        ans.append(1)
        continue
    dq.clear()
    for j in str:
        dq.append(j)
    preindex = 0
    index = preindex + 1
    while True:
        if index >= len(dq):
            break
        if dq[preindex]==dq[index]:
            if preindex==0:
                dq.popleft()
                dq.popleft()
            else:
                del dq[preindex]
                del dq[preindex] #!!!
                preindex -=1
                index -=1
        else:
            preindex +=1
            index +=1
    ans.append(len(dq))
for i in range(1,T+1):
    print("#{} {}".format(i,ans[i-1]))



