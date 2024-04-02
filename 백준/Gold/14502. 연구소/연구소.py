import sys
from collections import deque
from itertools import combinations as comb

sys.setrecursionlimit(10**6)

M,N = map(int,sys.stdin.readline().split())
Graph = [[i for i in list(map(int,sys.stdin.readline().split()))] for _ in range(M)]

space_list = []
virus_list = []
wall_list = []
for i in range(M):
  for j in range(N):
    if Graph[i][j]==0:
      space_list.append([i,j])
    elif Graph[i][j]==2:
      virus_list.append([i,j])
    else:
      wall_list.append([i,j])
wall_comb = list(comb(space_list,3))
    


def BFS_virus():
  bfs_queue = deque()
  min_unsafe=M*N
  for i in wall_comb:
    unsafe_count = 0
    visited = [[0 if Graph[m][n]==0 else 2 if Graph[m][n]==2 else 1 if Graph[m][n]==1 else None for n in range(N)] for m in range(M)]
    for j in i:
      visited[j[0]][j[1]]=1
    for v in virus_list:
      bfs_queue.append(v)
    while bfs_queue:
      v = bfs_queue.popleft()
      dx = [1,-1,0,0]
      dy = [0,0,1,-1]
      for i in range(4):
        moveX = v[0]+dx[i]
        moveY = v[1]+dy[i]
        if 0<=moveX<M and 0<=moveY<N and visited[moveX][moveY]==0:
          bfs_queue.append([moveX,moveY])
          visited[moveX][moveY]=1
          unsafe_count+=1
    if min_unsafe>unsafe_count:
      min_unsafe = unsafe_count
  return M*N - len(wall_list)-3 -len(virus_list) - min_unsafe
print(BFS_virus())
