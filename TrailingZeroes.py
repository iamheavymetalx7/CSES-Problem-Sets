#import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections

n=int(input())
a_,b_ =0,0
for i in range (1,n):
    a = math.floor(n/math.pow(5,i))
    if a==0:
        break
    a_+=a
    b_ +=math.floor(n/math.pow(2,i))
print(min(a_,b_))
