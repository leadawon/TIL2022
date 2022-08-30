'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
 


 

노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
 

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
 

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

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
2 5
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
#1 1
#2 1
#3 1	 
sample_output.txt
'''
import sys
from collections import deque

sys.stdin = open("testcase.txt","r")

T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    edge_dict = {}
    #{'1': ['4', '3'], '2': ['3', '5'], '4': ['6']}

    for j in range(E):
        a, b=input().split()
        if a in edge_dict:
            edge_dict[a].append(b)
        else:
            edge_dict[a]=[b]
    lst = list(input().split())

    #lst[0] : start node
    #lst[1] : end node

    visited = []
    dq = deque()

    v = lst[0]
    w = 0
    if v == lst[1]:
        print("#%s 1")
        continue
    visited.append(v)

    flag = False

    while v != 0:

        w = 0
        if v in edge_dict:
            for j in range(len(edge_dict[v])):
                if not (edge_dict[v][j] in visited):
                    w = edge_dict[v][j]
        if w != 0:
            dq.append(v)

        while w != 0:
            if w == lst[1]:
                flag = True
            visited.append(w)
            dq.append(w)
            v = w

            w = 0
            if v in edge_dict:
                for j in range(len(edge_dict[v])):
                    if not(edge_dict[v][j] in visited):
                        w = edge_dict[v][j]

        if len(dq) == 0:
            v = 0
        else:
            v = dq.pop()
    if flag == True:
        print("#%s 1" %(i+1))
    else:
        print("#%s 0" %(i+1))



'''
v에 start를 넣습니다. v를 방문합니다.
vistied리스트에 v를 넣습니다.
v의 인접정점중 visited리스트에 없는 것을 w에 저장합니다.
v를 스택에 저장합니다. 돌아올 정보를 저장하는 것입니다.

w를 방문하고 visited에 넣습니다. w를 스택에 넣습니다. v변수에 w를 붓습니다.
v의 인접정점주 visited하지 않은 정점을 찾아 w에 저장합니다. 바로 윗줄을 반복합니다.
이 반복은 v를 방문한 뒤 인접한 정점이 없을때 끝납니다.

스택에서 pop한것을 v에 넣습니다.(스택에서 원소가 없으면 dfs를 종료합니다.) 이 v에 대해서 인접한 정점을 찾습니다.
인접한 정점이 없으면 다시 스택에 pop합니다. 근데 인접한 정점이 있으면
이 정점을 w에 저장하고 v를 스택에 저장합니다.

w를 방문하고 visited에 넣습니다. w를 스택에 넣습니다. v변수에 w를 붓습니다.
v의 인접정점주 visited하지 않은 정점을 찾아 w에 저장합니다. 바로 윗줄을 반복합니다.
이 반복은 v를 방문한 뒤 인접한 정점이 없을때 끝납니다.

스택에서 pop한 것을 v에 넣습니다. 만약 pop할 원소가 없으면 dfs를 종료합니다.
'''
