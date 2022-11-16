'''
메모리 넘 많이 먹음
costarr는 0인덱스 일때만 10000 만큼의 메모리가 필요함
나머지 애들은... 4방향에 대한 메모리만 필요... 헐...'
나중에 시간 날때 풀어보자.
'''
import sys
n,m = map(int,sys.stdin.readline().split())

arr = []

#m행 n열
#0부터 오른족 끝 열 n-1열
for i in range(m):
    arr.append(list(sys.stdin.readline().rstrip()))
costarr = [[11111] * (m*n) for _ in range(m*n)]
for i in range(m):
    for j in range(n):
        costarr[n*i+j][n*i+j]=0
        if i != 0:
            if not costarr[n*i+j][n * (i-1) + j] == 1:
                costarr[n * i + j][n * (i - 1) + j] = 0
            costarr[n * (i-1) + j][n * i + j] = 0
        if j != n - 1:
            if not costarr[n * i + j][n*i + j + 1] == 1:
                costarr[n * i + j][n*i + j + 1] = 0
            #costarr[n * i + j][n*i + j + 1] = 0
            costarr[n*i + j + 1][n * i + j] = 0
        if i != m - 1:
            if not costarr[n * i + j][n * (i+1) + j] == 1:
                costarr[n * i + j][n * (i+1) + j] = 0
            #costarr[n * i + j][n * (i+1) + j] = 0
            costarr[n * (i+1) + j][n * i + j] = 0
        if j != 0:
            if not costarr[n * i + j][n*i + j - 1] == 1:
                costarr[n * i + j][n*i + j - 1] = 0
            #costarr[n * i + j][n*i + j - 1] = 0
            costarr[n*i + j - 1][n * i + j] = 0
        if arr[i][j]=="1":
            if i != 0:
                #costarr[n*i+j][n * (i-1) + j]=1
                costarr[n * (i-1) + j][n * i + j]=1
            if j != n-1:
                #costarr[n * i + j][n*i + j + 1]=1
                costarr[(n*i) + j + 1][n * i + j]=1
            if i != m-1:
                #costarr[n * i + j][(n * (i+1) + j]=1
                costarr[n * (i+1) + j][n * i + j]=1
            if j != 0:
                #costarr[n * i + j][n*i + j-1]=1
                costarr[n*i + j - 1][n * i + j]=1
del arr

print(costarr.shape)
visited = [False]*(m*n)
visited[0] = True
for i in range(m*n):
    min1 = 11111
    current = 0
    for j in range(m*n):
        if costarr[0][j] < min1 and visited[j] != True:
            min1 = costarr[0][j]
            current = j
    visited[current] = True
    for j in range(m*n):
        if (not visited[j]) and costarr[0][current]+costarr[current][j] < costarr[0][j]:
            costarr[0][j] = costarr[0][current]+costarr[current][j]
print(costarr[0][-1])
#print(costarr)


