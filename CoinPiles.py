import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
sys.setrecursionlimit(pow(10,9))


for testcase in range(int(input())):
    a,b = map(int, input().split())
    arr=[]
    def solve(a,b):
        if a<0 or b<0:
            arr.append(False)
            return
        if a==0 and b==0:
            arr.append(True)
            return
        solve(a-2,b-1)
        solve(a-1,b-2)
        return  
    solve(a,b)
    if any(arr):
        print("YES")
    else:
        print("NO")