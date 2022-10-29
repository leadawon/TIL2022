'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000	 
sample_input.txt
출력
#1 5
#2 5
#3 0	 
sample_output.txt
'''
import sys
sys.stdin = open("testcase.txt","r")

t = int(input())
answer = []
for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        slst = list(input())
        for k in range(n):
            slst[k] = int(slst[k])
        arr.append(slst)
    s_tp = (-1,-1)
    e_tp = (-1,-1)
    pter = [-1,-1]
    for j in range(n):
        for k in range(n):
            if arr[j][k] == 2:
                s_tp = (j,k)
                pter = [j,k]
            elif arr[j][k] == 3:
                e_tp = (j,k)
    #LEFT = -1
    #UP = -2
    #RIGHT = -3
    #DOWN = -4
    direction = [-5]
    iters = 0
    while True:
            if arr[pter[0]][pter[1]] == 3:
                #end
                iters *= -1
                iters -= 1
                break
            elif pter[1] != 0 and (arr[pter[0]][pter[1]-1] == 0 or arr[pter[0]][pter[1]-1] == 3):
                if arr[pter[0]][pter[1]] != 2:
                    arr[pter[0]][pter[1]] = iters
                pter[1] -= 1
                iters -= 1
                direction.append(-1)
                continue
            elif pter[0] != 0 and (arr[pter[0]-1][pter[1]] == 0 or arr[pter[0]-1][pter[1]] == 3):
                if arr[pter[0]][pter[1]] != 2:
                    arr[pter[0]][pter[1]] = iters
                pter[0] -= 1
                iters -= 1
                direction.append(-2)
                continue
            elif pter[1] != n-1 and (arr[pter[0]][pter[1]+1] == 0 or arr[pter[0]][pter[1]+1] == 3):
                if arr[pter[0]][pter[1]] != 2:
                    arr[pter[0]][pter[1]] = iters
                pter[1] += 1
                iters -= 1
                direction.append(-3)
                continue
            elif pter[0] != n-1 and (arr[pter[0]+1][pter[1]] == 0 or arr[pter[0]+1][pter[1]] == 3):
                if arr[pter[0]][pter[1]] != 2:
                    arr[pter[0]][pter[1]] = iters
                pter[0] += 1
                iters -= 1
                direction.append(-4)
                continue
            else:
                 #막혀있는 곳에서 이동할 곳이 있는 곳까지 이동하는 케이스와 첨까지 와서 더이상 이동할 수 없는 케이스
                    # if pter[1] == 0:
                    #     if pter[0] == 0:
                    #         pass
                    #     if pter[0] == n-1:
                    #         pass
                    #     else:
                    #         pass
                    # elif pter[0] == 0:
                    #     if pter[1] == n-1:
                    #         pass
                    #     else:
                    #         pass
                    # elif pter[1] == n-1:
                    #     if pter[0] == n-1:
                    #         pass
                    #     else:
                    #         pass
                    # elif pter[0] == n-1:
                    #     pass
                    # else:
                    #     pass
                ctr = direction.pop()
                if ctr == -5:
                    iters = 0
                    break
                elif ctr == -4:
                    arr[pter[0]][pter[1]] = 4
                    pter[0] -= 1
                    iters += 1
                elif ctr == -3:
                    arr[pter[0]][pter[1]] = 4
                    pter[1] -= 1
                    iters += 1
                elif ctr == -2:
                    arr[pter[0]][pter[1]] = 4
                    pter[0] += 1
                    iters += 1
                else:
                    arr[pter[0]][pter[1]] = 4
                    pter[1] += 1
                    iters += 1
    answer.append(iters)

for i in range(t):
    print(f"#{i+1} {answer[i]}")


