'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.
 

다음은 5x5 미로의 예이다.
 

13101

10101

10101

10101

10021

 

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
 

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

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
#1 1
#2 1
#3 0	 
sample_output.txt
'''
import sys
from collections import deque
# top right bottom left
def get_next(map,n , x, y, last_move):
    if x!=0 and map[x-1][y]!="1" and last_move!="b":
        return "t"
    elif y!=n-1 and map[x][y+1]!="1" and last_move!="l":
        return "r"
    elif x!=n-1 and map[x+1][y]!="1" and last_move!="t":
        return "b"
    elif y!=0 and map[x][y-1]!="1" and last_move!="r":
        return "l"
    else:
        return "f"
sys.stdin = open("testcase.txt","r")

T=int(input())
ans = []
for i in range(T):
    N = int(input())
    arr = []
    dq=deque()
    for j in range(N):
        arr.append(list(input()))
    for j in range(N):
        if "2" in arr[j]:
            locs = (j, arr[j].index("2"),"s")
        elif "3" in arr[j]:
            loce = (j, arr[j].index("3"),"e")
    #print(locs)
    #print(loce)
    dq.append(locs)
    control=get_next(arr, N,locs[0],locs[1],"none")
    xindex = locs[0]
    yindex = locs[1]
    move = None
    possible=None
    while True:
        #print("x는 {} 그리고 y는 {}".format(xindex,yindex))
        if control == "t":
            move="t"
            xindex-=1
            dq.append((xindex,yindex,move))
            if xindex==loce[0] and yindex==loce[1]:
                possible=True
                break
            control=get_next(arr, N, xindex,yindex,move)
        elif control == "r":
            move="r"
            yindex+=1
            dq.append((xindex,yindex,move))
            if xindex==loce[0] and yindex==loce[1]:
                possible=True
                break
            control=get_next(arr,N,xindex,yindex,move)
        elif control == "b":
            move = "b"
            xindex += 1
            dq.append((xindex, yindex, move))
            if xindex==loce[0] and yindex==loce[1]:
                possible=True
                break
            control = get_next(arr, N, xindex, yindex, move)
        elif control == "l":
            move = "l"
            yindex -= 1
            dq.append((xindex, yindex, move))
            if xindex==loce[0] and yindex==loce[1]:
                possible=True
                break
            control = get_next(arr, N, xindex, yindex, move)
        elif control == "f": #그리고 인덱스가 처음인덱스가 아닐때???
            if len(dq)==1:
                possible=False
                break
            popped_tuple=dq.pop()
            arr[xindex][yindex]="1"
            xindex=dq[-1][0]
            yindex=dq[-1][1]
            move=dq[-1][2]
            control=get_next(arr, N, xindex,yindex,move)

    #looooop end
    #print("-----1-1-1-1-1-1-1-------")
    if possible == True:
        ans.append(1)
    elif possible == False:
        ans.append(0)
for i in range(T):
    print("#{} {}".format(i+1,ans[i]))
