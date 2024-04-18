import sys

N = int(sys.stdin.readline())
DP = [0 for _ in range(N+1)]
DP[0],DP[1] = 1,1
for i in range(N+1):
  if i>=2:
    DP[i] = DP[i-1] + DP[i-2]
    
print(DP[-1]%10007)
# 2x0 : 1, 2x1 : 1, 2x2 : 2(||,=), 2x3 : 2x2+ 2x1*2(|||,=|,|=) = 4, 2x4 : 2x3 + 2x2 = 5 (||||,||=,|=|,=||,==)