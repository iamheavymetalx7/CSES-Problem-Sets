import sys
sys.stdout = open('CP_Oct/output.txt','w')
sys.stdin = open('CP_Oct/input.txt','r')
import math, itertools, collections

n = int(input()) 
arr = list(map(int, input().split()))
ans=[]
ct=0
for i in range(1,n):
    if arr[i-1]>arr[i]:
        ans.append(arr[i-1]-arr[i])
        arr[i]=arr[i-1]
        ct += arr[i-1]-arr[i]
print(sum(ans))

