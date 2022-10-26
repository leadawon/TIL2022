def quicksort(arr,i,j):
    if i>=j:
        return -1
    si = i
    sj = j
    p = j
    while True:
        if i<j:
            if arr[i]<arr[p]:
                i += 1
            elif arr[j]>arr[p]:
                j -= 1
            else:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        else:
            temp = arr[i]
            arr[i] = arr[p]
            arr[p] = temp
            quicksort(arr,si,i-1)
            quicksort(arr,i+1,sj)
            return 0
            
        


import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
quicksort(arr,0,n-1)
for i in range(n):
    sys.stdout.write(f"arr[i]\n")

    



            
    

    
    
            
    
