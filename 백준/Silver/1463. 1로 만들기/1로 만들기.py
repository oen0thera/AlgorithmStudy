import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
DP = [0]*(N+1)
result = 0

def dp_one():
  for i in range(2,N+1):
    DP[i]=DP[i-1]+1
    
    if i%2==0:
      DP[i] = min(DP[i],DP[i//2]+1)
      
    if i%3==0:
      DP[i] = min(DP[i],DP[i//3]+1)
      

dp_one()
print(DP[N])