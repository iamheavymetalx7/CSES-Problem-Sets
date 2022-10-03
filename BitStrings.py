import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')

n=int(input())
mod=pow(10,9)+7
ans=pow(2,n)%mod

print(ans)