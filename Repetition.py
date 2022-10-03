#import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections

s = str(input())
maxi=0
for x, y in itertools.groupby(s): 
    maxi=max(maxi,len(list(y)))
print(maxi)
