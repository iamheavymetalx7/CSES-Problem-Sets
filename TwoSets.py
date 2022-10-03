import sys
from timeit import timeit
sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections

n=int(input())
'''
3 = [1,2],[3]
4=[2,3],[1,4]
5 = [1,3,4],[2,5]
7 = [1,2,4,7],[3,5,6]
8 = [1,2,3,5,7],[8,6,4]
''' 
fir=[]
sec=[]
if (n*(n+1)*0.5)%2==1:
    print("NO")
else:

    print("YES")
    if n%2==0:
        for i in range(n//2):
            if(i%2==0):
                fir.append(i+1)
                fir.append(n-i)
            else:
                sec.append(i+1)
                sec.append(n-i)
    else:
        for i in range((n-1)//2):
            if(i%2==0):
                fir.append(i+1)
                fir.append(n-i-1)
            else:
                sec.append(i+1)
                sec.append(n-i-1)
        if len(fir)>len(sec):
            sec.append(n)
        else: 
            fir.append(n)
           
    print(len(fir))
    for i in fir:
        print(i,end=" ")
    print(" ")
    print(len(sec))
    for i in sec:
        print(i,end=" ")
