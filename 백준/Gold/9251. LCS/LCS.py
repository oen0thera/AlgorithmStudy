import sys
sys.setrecursionlimit(10**6)

Char_1 = sys.stdin.readline().strip()
Char_2 = sys.stdin.readline().strip()

def LCS():
    r = len(Char_1)
    c = len(Char_2)
    dp = [["" for _ in range(c + 1)] for _ in range(r + 1)]

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if Char_1[i - 1] == Char_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + Char_1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    return dp[r][c]

result = LCS()
print(len(result))