import sys
input = sys.stdin.readline

n = int(input())
n_list = []

for i in range(n):
    n_list.append(int(input()))

n_list.sort()

for i in n_list:
    print(i)

# 머지소트 구현

