import sys
sys.stdout = open('output.txt','w')
sys.stdin = open('input.txt','r')

sys.setrecursionlimit(pow(10,9))
import math, itertools, collections

s=str(input())
letters = list(s)
words=set()

def Permutation(word,letters):
    if len(letters)==1:
        words.add(word+letters[0])
    else:
        for i in range(len(letters)):
            Permutation(word+letters[i],letters[0:i]+letters[i+1:])

Permutation("",letters)

print(len(words))
print("\n".join(sorted(words)))