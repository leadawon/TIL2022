'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
 

3 4 + .
 

Forth에서는 동작은 다음과 같다.
 

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.

 

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
 

다음은 Forth 연산의 예이다.
 

코드

출력

4 2 / .

2

4 3 - .

1

 

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.

나눗셈의 경우 항상 나누어 떨어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

입력
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
 	 
sample_input.txt
출력
#1 84
#2 error
#3 168	 
sample_output.txt
'''
import sys
from collections import deque
sys.stdin = open("testcase.txt","r")

dq=deque()
ans = []
T=int(input())
for i in range(T):
    li=list(input().split())
    dq.clear()
    for j in li:
        if j.isdigit():
            dq.append(j)
            continue
        elif j==".":
            if len(dq)==1:
                ans.append(dq.pop())
                break ###
            else:
                ans.append("error")
                break
        elif len(dq)<=1:
            ans.append("error")
            break
        r=dq.pop()
        l=dq.pop()
        if r.isdigit() and l.isdigit():
            if j=="+":
                dq.append(str(int(l)+int(r)))
            elif j=="-":
                dq.append(str(int(l)-int(r)))
            elif j=="*":
                dq.append(str(int(l)*int(r)))
            elif j=="/":
                dq.append(str(int(l)//int(r)))
            else:
                ans.append("error")
                break
        else:
            ans.append("error")
            break
for i in range(T):
    print("#{} {}".format(i+1, ans[i]))