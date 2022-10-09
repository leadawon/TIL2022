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
