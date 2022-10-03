#import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections

n=int(input())

while(n!=1):
    print(int(n))
    if n%2==1:
        n=(3*n)+1
    else:
        n/=2
print(1)
