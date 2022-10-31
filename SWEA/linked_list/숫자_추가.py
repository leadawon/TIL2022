'''
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다.

이 수열은 완성된 것이 아니라 M개의 숫자를 지정된 위치에 추가하면 완성된다고 한다.

완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.

다음은 숫자를 추가하는 예이다.

 
인덱스

0

1

2

3

4

수열

1

2

3

4

5

 

2 7 -> 2번 인덱스에 7을 추가하고 한 칸 씩 뒤로 이동한다.
 

인덱스

0

1

2

3

4

5

수열

1

2

7

3

4

5



4 8 -> 4번 인덱스에 8을 추가하고 한 칸 씩 뒤로 이동한다.
 

인덱스

0

1

2

3

4

5

6

수열

1

2

7

3

8

4

5




[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.

그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
입력
3
5 2 5
1 2 3 4 5
2 7
4 8
5 5 4
13787 32221 32402 32498 4169
3 5902
3 9752
3 27737
1 14133
0 16547
10 10 8
16243 26767 22174 25277 17456 13398 29850 22297 1382 31246
9 23198
7 17514
11 24247
0 25306
2 9104
6 28112
12 7491
10 26972
17 22639
12 28722	 
sample_input.txt
출력
#1 4
#2 32402
#3 13398	 
sample_output.txt
'''
import sys
from collections import deque
sys.stdin = open("testcase.txt","r")

t = int(input().rstrip())
for i in range(t):
    n,m,l = map(int,input().split())

    lst = deque(map(int,input().split()))
    
    for j in range(m):
        ind,val = map(int,input().split())
        lst.insert(ind,val)
    print(f"#{i+1} {lst[l]}")
        


