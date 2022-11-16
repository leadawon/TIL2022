'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
2
'''
import sys
import heapq
from collections import deque
n, k = map(int, sys.stdin.readline().split())
heapque = []
visited = [0] * (k * 2)

sum1 = 0
if n > k:
    sum1 = n - k
elif n == k:
    n = k
else:
    visited[n] = 1
    #qu.append([0,2*n])
    #qu.append([1,n + 1])
    if n!=0:
        heapq.heappush(heapque,[0,2*n])
    heapq.heappush(heapque, [1,n + 1])
    visited[2 * n] = 1
    visited[n + 1] = 1
    if n > 0:

        #qu.append([1,n-1])
        heapq.heappush(heapque, [1,n-1])
        visited[n-1]=1
    while True:
        #info = qu.popleft()
        info = heapq.heappop(heapque)
        if info[1] == k:
            sum1 = info[0]
            break
        else:
            if info[1] < k:
                if visited[info[1] + 1] == 0 or visited[info[1] + 1] > info[0]+1:

                    #qu.append([ info[0] + 1, info[1] + 1])
                    heapq.heappush(heapque, [ info[0] + 1, info[1] + 1])

                    visited[info[1] + 1] = info[0]+1
                if (visited[info[1] * 2] == 0 or visited[info[1] * 2] > info[0]) and info[1] != 0:
                    #qu.append([info[0],info[1] * 2])
                    heapq.heappush(heapque,[info[0],info[1] * 2])
                    visited[info[1] * 2] = info[0]
                if info[1] != 0 and (visited[info[1] - 1] == 0 or visited[info[1] - 1] > info[0]+1):
                    #qu.append([info[0] + 1,info[1] - 1])
                    heapq.heappush(heapque, [info[0] + 1,info[1] - 1])
                    visited[info[1] - 1] = info[0]+1
            elif info[1] != 0 and (visited[info[1] - 1] == 0 or visited[info[1] - 1] > info[0]+1):
                #qu.append([info[0] + 1,info[1] - 1])
                heapq.heappush(heapque, [info[0] + 1,info[1] - 1])
                visited[info[1] - 1] = info[0]+1

sys.stdout.write(f"{sum1}")





