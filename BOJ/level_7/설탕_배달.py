'''
문제
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

출력
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

예제 입력 1 
18
예제 출력 1 
4
예제 입력 2 
4
예제 출력 2 
-1
예제 입력 3 
6
예제 출력 3 
2
예제 입력 4 
9
예제 출력 4 
3
예제 입력 5 
11
예제 출력 5 
3
'''
n=int(input())
cnt=0
if n%5==0:
    print(int(n/5))
elif n==3:
    print(1)
elif n==4:
    print(-1)
elif n==5:
    print(-1)
elif n==6:
    print(2)
elif n==7:
    print(-1)
elif n==8:
    print(2)
elif n==9:
    print(3)
elif n==10:
    print(2)
elif n==11:
    print(3)
elif n==12:
    print(4)
else:
    while True:
        n-=5
        cnt+=1
        if n>=13:
            continue
        else:
            if n==8:
                cnt+=2
                break
            elif n==9:
                cnt+=3
                break
            elif n==10:
                cnt+=2
                break
            elif n==11:
                cnt+=3
                break
            else:#n==12
                cnt+=4
                break
    print(cnt)  
        
                    
                
            

        
    
