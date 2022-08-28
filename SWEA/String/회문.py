'''
 

ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ	 
sample_input.txt
출력
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT	 
sample_output.txt
'''
import sys
sys.stdin = open("testcase.txt","r")

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = [" " for i in range(N)]
    flag = False
    ans = []
    for j in range(N):
        arr[j] = list(input())
    #가로로
    for j in range(N):
        for k in range(N-M+1):
            ind = 0
            while True:
                if arr[j][k + ind] == arr[j][k + (M - 1) - ind]:
                    if ind >= M-1-ind:
                        ans = arr[j][k:k+(M-1)+1]
                        flag = True
                        break
                    else:
                        ind += 1
                else:
                    break
            if flag == True:
                break
        if flag == True:
            break

    #세로로
    for j in range(N):
        for k in range(N-M+1):
            ind = 0
            while True:
                if arr[k + ind][j] == arr[k + (M - 1) - ind][j]:
                    if ind >= M - 1 - ind:
                        #ans = arr[k:k + (M - 1) + 1][j]
                        for l in range(k, k+(M-1+1)):
                            ans.append(arr[l][j])
                        flag = True
                        break
                    else:
                        ind += 1
                else:
                    break
            if flag == True:
                break
        if flag == True:
            break

    print("#%s" %(i+1),end=" ")
    print(''.join(ans))

