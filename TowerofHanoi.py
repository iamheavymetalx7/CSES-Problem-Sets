import sys
sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections
sys.setrecursionlimit(pow(10,9))

n=int(input())

def TOH(src, dest, helper,n):
    if n==0:
        return 0
    TOH(src,helper,dest,n-1)
    arr.append([src,dest])
    TOH(helper,dest,src,n-1)

arr=[]
TOH(1,3,2,n)
print(len(arr))
for i in range(len(arr)):
    print(arr[i][0]," ",arr[i][1])
