'''
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.

다음은 리프 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.
  
	
리프 노드 저장 값	자식 노드의 합을 저장한 상태

N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.

완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.

리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L이 주어지고, 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 

입력
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962	 
sample_input.txt
출력
#1 3
#2 845
#3 1801	 
sample_output.txt
'''
import sys
from collections import deque

sys.stdin = open("testcase.txt","r")

t = int(input())

for i in range(t):
    n,m,l = map(int,input().split())
    arr = [0]*(n+1)
    ind_collecter = deque()
    for j in range(m):
        ind_leaf , item_leaf = map(int,input().split())
        arr[ind_leaf] = item_leaf
        ind_collecter.append(ind_leaf)
    while ind_collecter:
        leaf_ind = ind_collecter.popleft()
        if leaf_ind == 1:
            continue
        if leaf_ind%2 ==0:
            if leaf_ind == n:
                arr[leaf_ind//2] = arr[leaf_ind]
                ind_collecter.append(leaf_ind // 2)
            elif arr[leaf_ind+1] != 0:
                arr[leaf_ind//2] = arr[leaf_ind] + arr[leaf_ind+1]
                ind_collecter.append(leaf_ind // 2)
        elif leaf_ind%2 == 1 and arr[leaf_ind-1] !=0:
            arr[leaf_ind//2] = arr[leaf_ind] + arr[leaf_ind-1]
            ind_collecter.append(leaf_ind//2)
        else:
            ind_collecter.append(leaf_ind)
    print(f"#{i+1} {arr[l]}")
