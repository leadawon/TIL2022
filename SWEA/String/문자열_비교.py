'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
 

ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
 

ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
 

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



 
입력
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW	 
sample_input.txt
출력
#1 1
#2 0
#3 1	 
sample_output.txt
'''
import sys
sys.stdin = open("testcase.txt","r")

T=int(input())
for i in range(T):
    pat = list(input().rstrip())
    lngstr = list(input().rstrip())
    skip = {}
    flag = False
    for j in range(ord('A'), ord('Z')+1):
        skip[chr(j)] = len(pat)

    for j in range(len(pat)):
        skip[pat[j]] = len(pat)-j-1

    lngstr_header = 0
    pat_header = len(pat)-1
    temp = 0
    while True:
        if lngstr[lngstr_header] == pat[pat_header]:
            if pat_header == 0:
                flag = True
                break
            elif lngstr_header != 0: #아직 검사해야할 패턴과 주어진 스트링이 남아있을때 역행하면서 검사할것이다.
                if temp != lngstr_header and pat_header == len(pat)-1: #역행하기전 꼬리부분 저장
                    temp = lngstr_header
                pat_header -= 1
                lngstr_header -= 1
                continue
            else: #검사해야할 패턴이 남아있지만 주어진 스트링의 앞부분으로 거슬러 올라갈 부분이 없을때
                lngstr_header = temp + 1
                if lngstr_header > len(lngstr) - 1:
                    break
                pat_header = len(pat)-1
                continue
        elif lngstr_header == len(lngstr)-1: #끝까지 가봤는데 같은 부분이 없을때
            break
        elif pat_header == len(pat)-1:  #끝부분이 다를때, 일반적으로 틀린 경우, 점프해야 하는경우
            lngstr_header += skip[lngstr[lngstr_header]]
            if lngstr_header > len(lngstr)-1:
                break
            continue

        else: #패턴의 끝부분이 일치함을 보였고 다음 패턴을 확인하던 중에 패턴과 스트링의 비교부분이 다를떄
            lngstr_header = temp + 1          #이 1을 바꿀수 없을까? 더 좋은 방법이 있긴 할듯...
            if lngstr_header > len(lngstr) - 1:
                break
            pat_header = len(pat) - 1

    if flag==True:
        print("#%s 1" %(i+1))
    else:
        print("#%s 0" %(i+1))


