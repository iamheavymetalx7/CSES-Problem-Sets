import sys
sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')

'''
this code is for checking how the solution behaves.
the next part contains the key idea taken from these outputs.
'''
import math, itertools, collections

n=int(input())

a=(list(itertools.permutations(range(1,n+1))))
for i in range(len(a)):
    arr=[]
    for j in range(len(a[i])-1):
        if abs(a[i][j+1]-a[i][j])>1:
            arr.append(1)
        else:
            arr.append(0)
    if all(arr):
        ar2=a[i]
        break
    else:
        print("NO SOLUTION")
if (ar2):
    for i in ar2:
        print(i,end=" ")