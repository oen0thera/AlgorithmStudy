import sys

N = int(sys.stdin.readline())
count = 0
board = [0]*N

def N_Queen(r):
  global count
  if (r==N):
    count+=1
    return
  else:
    for c in range(N):
      board[r] = c
      if next_queen(r):
        N_Queen(r+1)

def next_queen(r):
  for i in range(r):
    if board[r]==board[i] or abs(board[r]-board[i])==abs(r-i):
      return False
  return True

N_Queen(0)
print(count)