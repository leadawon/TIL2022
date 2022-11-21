'''
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

16진수 A부터 F는 대문자로 표시된다.
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
4 47FE
5 79E12
8 41DA16CD	


 
sample_input.txt
출력
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101	 
sample_output.txt
'''
def bina(n):
  str1=""
  if not n.isdigit():
    n=ord(n)-55
  n=int(n)
  for i in range(4):
      str1+=str(n%2)
      n=n//2
  return str1[::-1]



t = int(input())

for i in range(t):
  result = ""
  n,lst = input().split()

  for j in list(lst):
    result += bina(j)
  print(f"#{i+1} {result}")
