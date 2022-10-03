import sys
#sys.stdout = open('CSES ProblemSet/Graph Algos/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Graph Algos/input.txt','r')
import itertools,math,collections

a,b = map(int,input().split())
arr = [[0 for i in range(b)] for i in range(a)]
sys.setrecursionlimit(pow(10,9))

for i in range(a):
    s=str(input())
    s=list(s)
    for j in range(b):
        arr[i][j]=s[j]
#print("is this code running?")
def solve(r,c,n,m,arr):
    if (r<0 or c<0 or r>=n or c>=m or arr[r][c]!='.'):
        return
    arr[r][c]="#"
    #print(arr)
    solve(r-1,c,n,m,arr)#left
    solve(r+1,c,n,m,arr)#right
    solve(r,c+1,n,m,arr)#top
    solve(r,c-1,n,m,arr)#bottom

def Countrooms(arr,a,b):
    if a==0:
        print(0)
    ans=0
    for i in range(a):
        for j in range(b):
            if arr[i][j]=='.':
                solve(i,j,a,b,arr)
                ans=ans+1
    print(ans)
Countrooms(arr,a,b)
