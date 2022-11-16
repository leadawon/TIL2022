'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17
'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
qu = deque()
ndarr = []
visited = [0] * (k * 2)
answer = []

sum1 = 0
if n > k:
    sum1 = n - k
    sys.stdout.write(f"{sum1}\n")
    for i in range(n,k-1,-1):
        sys.stdout.write(f"{i} ")
    #####
elif n == k:

    sys.stdout.write(f"0\n{n}")
    ####
else:
    visited[n] = 1
    ndarr.append([0])
    # pre_location, now_location
    ndarr[0].append((-1,n))
    # location, count, pre_location
    qu.append([2 * n, 1,n])
    qu.append([n + 1, 1,n])
    visited[2 * n] = 1
    visited[n + 1] = 1
    rememberinfo = []
    if n > 0:
        qu.append([n-1,1,n])
        visited[n-1]=1
    while True:
        info = qu.popleft()
        if info[1] == len(ndarr):
            ndarr.append([info[1]])

        ndarr[info[1]].append((info[2],info[0]))

        if info[0] == k:
            sum1 = info[1]
            rememberinfo = info
            break
        else:
            if info[0] < k:
                if visited[info[0] + 1] == 0:
                    qu.append([info[0] + 1, info[1] + 1,info[0]])
                    visited[info[0] + 1] = 1
                if visited[info[0] * 2] == 0:
                    qu.append([info[0] * 2, info[1] + 1,info[0]])
                    visited[info[0] * 2] = 1
                if info[0] != 0 and visited[info[0] - 1] == 0:
                    qu.append([info[0] - 1, info[1] + 1,info[0]])
                    visited[info[0] - 1] = 12
            elif info[0] != 0 and visited[info[0] - 1] == 0:
                qu.append([info[0] - 1, info[1] + 1,info[0]])
                visited[info[0] - 1] = 1
    last = k
    for i in range(rememberinfo[1],-1,-1):
        for j in range(1,len(ndarr[i])):
            if ndarr[i][j][1] == last:
                answer.append(last)
                last = ndarr[i][j][0]
                break

    sys.stdout.write(f"{sum1}\n")
    for i in range(len(answer)-1,-1,-1):
        sys.stdout.write(f"{answer[i]} ")






