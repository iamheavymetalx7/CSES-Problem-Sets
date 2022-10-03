import sys
#from timeit import timeit
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections

n=int(input())
'''
https://japlslounge.com/posts/cses/two_knights/1.htm
'''
'''
https://www.codespeedy.com/the-two-knights-problem-implemented-in-c/#:~:text=So%2C%20k2%3D%20n*n,k1*(k1%2D1).
'''
for i in range(1,n+1):
    k=pow(i,2)

    ans=k*(k-1)*0.5-(4*(i-1)*(i-2))
    print(int(ans))
