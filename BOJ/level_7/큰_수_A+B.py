'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)

출력
첫째 줄에 A+B를 출력한다.

예제 입력 1 
9223372036854775807 9223372036854775808
예제 출력 1 
18446744073709551615
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: dlaud5379, gcon16
문제의 오타를 찾은 사람: jh05013
알고리즘 분류
수학
구현
사칙연산
임의 정밀도 / 큰 수 연산
'''
a,b=input().split()
a=int(a)
b=int(b)

print(a+b)
