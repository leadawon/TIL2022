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









