import sys

N = int(sys.stdin.readline())

Cards = list(map(int,sys.stdin.readline().split()))
DP = [0]+Cards

def dp_card():
  #print("카드는 1부터 시작되며, 프린트시 편의상 번호가 곧 카드개수")
  for i in range(1,N):
    for j in range(i):
      #print("Cards[",i+1,"] =",Cards[i],"<-> DP[",i-j,"]+Cards[",j+1,"] =",DP[i-j]+Cards[j]," DP:", DP)
      max_pay = max(Cards[i],DP[i-j]+Cards[j])
      if max_pay>DP[i+1]:
        DP[i+1]=max_pay
dp_card()
print(max(DP))