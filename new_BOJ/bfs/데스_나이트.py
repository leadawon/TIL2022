'''
문제
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
7
6 6 0 1
예제 출력 1 
4
예제 입력 2 
6
5 1 0 5
예제 출력 2 
-1
예제 입력 3 
7
0 3 4 3
예제 출력 3 
2
'''
import sys
from collections import deque
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

r1,c1,r2,c2 = map(int,sys.stdin.readline().split())

visited = defaultdict(int)

qu = deque()
#location of row and col , count
qu.append([r1,c1,0])
sum1 = -1
while qu:
    item = qu.popleft()
    if item[0] == r2 and item[1] == c2:
        sum1 = item[2]
        break
    if not visited[(item[0]-2,item[1]-1)] and item[0]-2 >= 0 and item[1]-1 >= 0:
        qu.append([item[0]-2,item[1]-1,item[2]+1])
        visited[(item[0]-2,item[1]-1)]=1
        
    if not visited[(item[0]-2,item[1]+1)] and item[0]-2>=0 and item[1]+1<=n-1:
        qu.append([item[0]-2,item[1]+1,item[2]+1])
        visited[(item[0]-2,item[1]+1)]=1
        
    if not visited[(item[0],item[1]-2)] and item[1]-2>=0:
        qu.append([item[0],item[1]-2,item[2]+1])
        visited[(item[0],item[1]-2)]=1
        
    if not visited[(item[0],item[1]+2)] and item[1]+2<=n-1:
        qu.append([item[0],item[1]+2,item[2]+1])
        visited[(item[0],item[1]+2)]=1
        
    if not visited[(item[0]+2,item[1]-1)] and item[0]+2<=n-1 and item[1]-1>=0:
        qu.append([item[0]+2,item[1]-1,item[2]+1])
        visited[(item[0]+2,item[1]-1)]=1
        
    if not visited[(item[0]+2,item[1]+1)] and item[0]+2<=n-1 and item[1]+1<=n-1:
        qu.append([item[0]+2,item[1]+1,item[2]+1])
        visited[(item[0]+2,item[1]+1)]=1
if r1==r2 and c1==c2:
    sys.stdout.write("0")
else:
    sys.stdout.write(f"{sum1}")
