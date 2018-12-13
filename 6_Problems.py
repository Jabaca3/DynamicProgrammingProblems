'''
Created on Dec 10, 2018

@author: Joseph Baca
'''

#https://leetcode.com/problems/stone-game/submissions/

def stoneGame(p):
    n = len(p)
    dp = [[0] * n for i in range(n)]
    for i in range(n): dp[i][i] = p[i]
    
    for d in range(1, n):
        for i in range(n - d):
            dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
    return dp[0][-1] > 0
    
    

def minFallingPathSum(self, A):
    for row in A:
        row.append(101)
        row.insert(0, 101)
        
    for i in range(1, len(A)):
        for j in range(1, len(A[0]) - 1):
            A[i][j] += min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
    
    return min(A[-1])


def arithmaticSlices(A):
    
    res = [0]
    count = 1
    
    for i in range (2,len(A)):
        if A[i] - A[i-1] == A[i-1]-A[i-2]:
            res.append(res[-1]+count)
            count+=1
        else:
            count = 1
            
    return res[-1]
   
   
def minimumDeleteSum(s1, s2):
       
    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    print(sum(map(ord, s1 + s2)))
    print(dp[l1][l2] * 2)
    result = sum(map(ord, s1 + s2)) - dp[l1][l2] * 2
    return result


def integerBreak(self, n):
    
        if n == 2: return 1
        res = [1] * (n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                _max = max(j * res[i-j], j * (i-j))
                res[i] = max(res[i], _max)
        return res[n]
    
    
def countSubstrings(self, s):

        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                
        for d in range(2, n):
            for i in range(n-d):
                
                if dp[i+1][i+d-1]:
                    if s[i] == s[i+d]:
                        dp[i][i+d] = 1
                
        return sum([dp[i][j] for i in range(n) for j in range(n)])
    
    
    
'''
Testing Solutions:

piles = [5,3,4,15]

array = [1,2,3,4,6,5]
print(stoneGame(piles))
print(arithmaticSlices(array))
print(array[-1])

print(getMaxIndex(piles))

#piles.remove(getMaxIndex(piles))
piles.pop(3)
print(piles)
'''

