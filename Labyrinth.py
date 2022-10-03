import sys
sys.stdout = open('CSES ProblemSet/Graph Algos/output.txt','w')
sys.stdin = open('CSES ProblemSet/Graph Algos/input.txt','r')
import itertools,math,collections

a,b = map(int,input().split())
arr = [[0 for i in range(b)] for i in range(a)]
sys.setrecursionlimit(pow(10,9))

for i in range(a):
    s=str(input())
    s=list(s)
    for j in range(b):
        arr[i][j]=s[j]

def solve(stx,sty,endx,endy,a,b,arr,s,ans):
    if stx<0 or sty<0 or stx>=a or sty>=b or arr[stx][sty]=='#':
        return ""


    if (stx==endx and sty==endy):
        ans.append(s)
        return

    current=arr[stx][sty]
    arr[stx][sty]='#'

    solve(stx+1,sty,endx,endy,a,b,arr,s+'D',ans)
    solve(stx-1,sty,endx,endy,a,b,arr,s+'U',ans)
    solve(stx,sty-1,endx,endy,a,b,arr,s+'L',ans)
    solve(stx,sty+1,endx,endy,a,b,arr,s+'R',ans)
    arr[stx][sty]=current
    return

def Labyrinth(arr,a,b):
    ans=[]
    for i in range(a):
        for j in range(b):
            if arr[i][j]=='A':
                stx,sty=i,j
            if arr[i][j]=='B':
                endx,endy=i,j
    solve(stx,sty,endx,endy,a,b,arr,"",ans)
    if len(ans)>0:
        print("YES")
        length=float('inf')
        index=0
        for i in range(len(ans)):
            if len(ans[i])<length:
                length=len(ans[i])
                index=i
        print(len(ans[index]))
        print(ans[index])
    else:
        print("NO")
        



Labyrinth(arr,a,b)

