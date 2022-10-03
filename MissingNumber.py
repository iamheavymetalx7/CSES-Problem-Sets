#import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections

n=int(input())
b = [*map(int, input().split())]

total_sum = n*(n+1)*0.5
print(int(total_sum-sum(b)))
