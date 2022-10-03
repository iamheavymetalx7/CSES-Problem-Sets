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
'''
The thing to note here is that, for any 4 
consecutive numbers, the sum of 1st and 4th = sum of 2nd and 3rd.

now if n=3: we divide it into [1,2] [3] and then work accordingly.
'''

summ=n*(n+1)*0.5

if summ%2!=0:
    print("NO")
    
