'''
import sys
from collections import deque
import copy



sys.stdin = open("testcase.txt","r")
T = int(input())
ans = []
for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(list(map(int,input().split())))

    permu = [j for j in range(N)]
    used = [0 for j in range(N)]

    dq = deque()
    #dq.clear()
    def generate(chosen, used):
        if len(chosen) == N:
            dq.append(copy.deepcopy(chosen))
            return 0

        for i in range(N):
            if not used[i]:
                chosen.append(permu[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
        return 0
    chosen = deque()
    generate(chosen , used)

    min=0
    for j in range(N):
        min+=arr[j][dq[0][j]]

    for j in range(len(dq)):
        sum = 0
        for k in range(N):
            sum += arr[k][dq[j][k]]
        if sum < min:
            min = sum
    ans.append(min)

for i in range(T):
    print("#{} {}".format(i+1, ans[i]))

#what the....

NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
 

예를 들어 다음과 같이 배열이 주어진다.
 

2

1

2

5

8

5

7

2

2



이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

입력
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8	 
sample_input.txt
출력
#1 8
#2 14
#3 9	 
sample_output.txt
'''
import sys
from collections import deque
import copy



sys.stdin = open("testcase.txt","r")
T = int(input())
ans = []
for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(list(map(int,input().split())))

    permu = [j for j in range(N)]
    used = [0 for j in range(N)]

    min = [0]
    min[0] = 0
    for j in range(N):
        min[0] += arr[j][j]

    def generate(chosen, used, min):
        sum = 0
        for j in range(len(chosen)):
            sum += arr[j][chosen[j]]
        if sum > min[0]:
            return -400
        if len(chosen) == N:
            sum = 0
            for j in range(N):
                sum += arr[j][chosen[j]]
            if sum < min[0]:
                min[0] = sum
            return -300

        for i in range(N):
            if not used[i]:
                chosen.append(permu[i])
                used[i] = 1
                generate(chosen, used,min)
                used[i] = 0
                chosen.pop()
        return -200
    chosen = deque()
    generate(chosen , used,min)
    ans.append(min[0])
for i in range(T):
    print("#{} {}".format(i+1, ans[i]))


