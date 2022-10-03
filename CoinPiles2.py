import sys
#sys.stdout = open('CSES ProblemSet/Introductory Problems/output.txt','w')
#sys.stdin = open('CSES ProblemSet/Introductory Problems/input.txt','r')
sys.setrecursionlimit(pow(10,9))

'''
https://www.geeksforgeeks.org/check-if-two-piles-of-coins-can-be-emptied-by-repeatedly-removing-2-coins-from-a-pile-and-1-coin-from-the-other/
'''

'''
Therefore, the idea is to check if the sum of 
total number of coins is a multiple of 3 and 
the maximum number of coins is at most twice
the minimum number of coins, then print “Yes”. 
Otherwise, print “No”.
'''

for testcase in range(int(input())):
    a,b = map(int, input().split())


    def canBeEmptied(A, B):

        if (max(A, B) > 2 * min(A, B)):
            print("NO")
            return

        if ((A + B) % 3 == 0):
            print("YES")
        else:
            print("NO")
    canBeEmptied(a,b)