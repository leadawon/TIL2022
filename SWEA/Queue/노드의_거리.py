'''
틀린코드
'''
import sys
from collections import deque
sys.stdin = open("testcase.txt","r")


t = int(input())
for i in range(t):
    v,e = map(int,input().split())
    arcs = [[0]*v for _ in range(v)]
    for j in range(e):
        arcst,arcen = map(int,input().split())
        arcs[arcst-1][arcen-1] = 1
        arcs[arcen-1][arcst-1] = 1
    startnode,endnode = map(int,input().split())
    startnode -= 1
    endnode -= 1

    q = deque([startnode])
    his = [(-1,startnode)]
    while q:
        ctr = q.popleft()
        for j in range(v):
            if arcs[ctr][j] == 1:
                q.append(j)
                his.append((ctr,j))
                arcs[ctr][j] = -1
                arcs[j][ctr] = -1
                if j == endnode:
                    q.clear()
                    break
    iters = 0
    if his[-1][1] == endnode:
        ctr=his[-1][0]
        iters = 1
        te = 1
        while ctr != startnode:
            for j in range(te,len(his)+1):
                if his[-j][1] == ctr:
                    iters += 1
                    te = j
                    ctr = his[-j][0]
                    break
        print(f"#{i+1} {iters}")
    else:
        print(f"#{i+1} {iters}")



#################################
#bfs
#################################
'''
right code
'''
'''

V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.


   

 
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.

E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

 

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9	 
sample_input.txt
출력
#1 2
#2 4
#3 3	 
sample_output.txt
'''
import sys
from collections import deque
sys.stdin = open("testcase.txt","r")
def bfs(start,end,arcs):
    q = deque([start])
    vs = [0]*len(arcs)
    vs[start] = 1

    while q:
        ctr = q.popleft()
        for index in range(len(arcs)):
            if arcs[ctr][index] == 1 and vs[index] == 0:
                vs[index] = vs[ctr] + 1
                q.append(index)
                if index == end:
                    return vs[index] - 1
    return 0
t = int(input())
for i in range(t):
    v,e = map(int,input().split())
    arcs = [[0]*v for _ in range(v)]
    for j in range(e):
        arcst,arcen = map(int,input().split())
        arcs[arcst-1][arcen-1] = 1
        arcs[arcen-1][arcst-1] = 1
    startnode,endnode = map(int,input().split())
    startnode -= 1
    endnode -= 1
    ans = bfs(startnode,endnode,arcs)
    print(f"#{i+1} {ans}")








