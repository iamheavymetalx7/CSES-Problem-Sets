import sys
sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
import math, itertools, collections


for testcase in range(int(input())):
    a = [*map(int, input().split())]
    print(a[0],a[1])