'''
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
 

1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.

그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

 

  i

 

 

 

 

     (i+j)//2

    (i+j)//2+1

 

 

 

 j

 

 

 

 

…

 

 

 

 

 

 

…

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 



두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.

다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.

 

 

 

 

 

 

 

 

 

 

2

 

 

 

 

 

↗

 

↖

 

 

 

1

 

 

 

2

 

↗

 

↖

 

↗

 

↖

1

 

3

 

2

 

1

1

 

2

 

3

 

4

 


N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100

카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.

입력
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3	 
sample_input.txt
출력
#1 3
#2 5
#3 1	 
sample_output.txt
'''
import sys
from collections import deque
import copy
class Node:
    def __init__(self, s,e,p,d):
        self.start = s
        self.end = e
        self.left = None
        self.right = None

        self.parent = p
        self.direction = d

        self.leftkey = None
        self.rightkey = None

    def get_start(self):
        return int(self.start)

    def get_end(self):
        return int(self.end)

    def get_direction(self):
        return self.direction

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def get_direction(self):
        return self.direction

    def get_rightkey(self):
        return self.rightkey

    def get_leftkey(self):
        return self.leftkey



    def set_leftkey(self, k):
        self.leftkey = k

    def set_rightkey(self, k):
        self.rightkey = k

    def postorder(self):
        traverse = deque()
        if self.left:
            traverse+=(self.left.postorder())
        if self.right:
            traverse+=(self.right.postorder())
        traverse.append(self)
        return traverse
class Btree:
    def __init__(self):
        self.root=None
        self.size = 0

    def make_left_node(self,s,e,p):

        new_node = Node(s,e,p,"left")
        p.left = new_node
        self.size += 1
        return new_node

    def make_right_node(self,s,e,p):

        new_node = Node(s,e,p,"right")
        p.right = new_node
        self.size += 1
        return new_node

    def set_root_node(self,root):
        self.root=root

    def delete_node(self,node):
        del node
        self.size -= 1

    def get_size(self):
        return self.size

    def get_root(self):
        return self.root

sys.stdin = open("testcase.txt","r")

T = int(input())
ans = []
for i in range(T):
    N = int(input())
    value = list(map(int, input().split()))
    game_tree = Btree()

    root_node = Node(1,N,None,"root")
    game_tree.set_root_node(root_node)

    dq = deque()
    dq.clear()

    dq.append(root_node)
    while len(dq)!=0:
        if dq[0].get_start() == dq[0].get_end():
            dq.popleft()
        else:
            a = (dq[0].get_start()+dq[0].get_end())//2
            dq.append(game_tree.make_left_node(dq[0].get_start(),a,dq[0]))
            dq.append(game_tree.make_right_node(a+1, dq[0].get_end(), dq[0]))
            dq.popleft()

    dq = game_tree.get_root().postorder()
    while len(dq) != 1:

        if dq[0].get_start() == dq[0].get_end():
            if dq[0].get_direction() == "left":
                dq[0].get_parent().set_leftkey(dq[0].get_start())
            elif dq[0].get_direction() == "right":
                dq[0].get_parent().set_rightkey(dq[0].get_start())
            else:
                print("error")
            dq.popleft()
        elif dq[0].get_leftkey() != None and dq[0].get_rightkey() != None:
            if dq[0].get_leftkey() > dq[0].get_rightkey():
                print("no answer")
            if value[dq[0].get_leftkey()-1] == value[dq[0].get_rightkey()-1]:
                if dq[0].get_direction() == "left":
                    dq[0].get_parent().set_leftkey(dq[0].get_leftkey())
                elif dq[0].get_direction() == "right":
                    dq[0].get_parent().set_rightkey(dq[0].get_leftkey())
                else:
                    print("error")
            elif value[dq[0].get_leftkey()-1] < value[dq[0].get_rightkey()-1]:
                if value[dq[0].get_rightkey()-1] == 3 and value[dq[0].get_leftkey()-1] == 1:
                    if dq[0].get_direction() == "left":
                        dq[0].get_parent().set_leftkey(dq[0].get_leftkey())
                    elif dq[0].get_direction() == "right":
                        dq[0].get_parent().set_rightkey(dq[0].get_leftkey())
                    else:
                        print("error")
                else:
                    if dq[0].get_direction() == "left":
                        dq[0].get_parent().set_leftkey(dq[0].get_rightkey())
                    elif dq[0].get_direction() == "right":
                        dq[0].get_parent().set_rightkey(dq[0].get_rightkey())
                    else:
                        print("error")
            elif value[dq[0].get_leftkey()-1] > value[dq[0].get_rightkey()-1]:
                if value[dq[0].get_rightkey() - 1] == 1 and value[dq[0].get_leftkey() - 1] == 3:
                    if dq[0].get_direction() == "left":
                        dq[0].get_parent().set_leftkey(dq[0].get_rightkey())
                    elif dq[0].get_direction() == "right":
                        dq[0].get_parent().set_rightkey(dq[0].get_rightkey())
                    else:
                        print("error")
                else:
                    if dq[0].get_direction() == "left":
                        dq[0].get_parent().set_leftkey(dq[0].get_leftkey())
                    elif dq[0].get_direction() == "right":
                        dq[0].get_parent().set_rightkey(dq[0].get_leftkey())
                    else:
                        print("error")
            else:
                print("nonono~~")

            dq.popleft()
        else:
            print("no dab")

    if dq[0].get_rightkey() == None:
        print(dq[0].get_leftkey())
    elif dq[0].get_leftkey() == None:
        print(dq[0].get_rightkey())
    else:
        if dq[0].get_leftkey() > dq[0].get_rightkey():
            print("no answer")
        if value[dq[0].get_leftkey() - 1] == value[dq[0].get_rightkey() - 1]:
            ans.append(dq[0].get_leftkey())
        elif value[dq[0].get_leftkey() - 1] < value[dq[0].get_rightkey() - 1]:
            if value[dq[0].get_rightkey() - 1] == 3 and value[dq[0].get_leftkey() - 1] == 1:
                ans.append(dq[0].get_leftkey())
            else:
                ans.append(dq[0].get_rightkey())
        elif value[dq[0].get_leftkey() - 1] > value[dq[0].get_rightkey() - 1]:
            if value[dq[0].get_rightkey() - 1] == 1 and value[dq[0].get_leftkey() - 1] == 3:
                ans.append(dq[0].get_rightkey())
            else:
                ans.append(dq[0].get_leftkey())
        else:
            print("error")
for i in range(T):
    print("#{} {}".format(i+1, ans[i]))


