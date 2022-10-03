import sys
sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')


import math, itertools, collections

n=int(input())
if n==1:
    print(1)
if n==4:
    print("2 4 1 3")
if n in [2,3]:
    print("NO SOLUTION")
if n>=5:
    for i in range(1,n+1):
        if(i%2==1):
            print(i,end=" ")

    for i in range(1,n+1):
        if (i%2==0):
            print(i,end=" ")