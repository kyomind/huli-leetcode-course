import sys
lines = sys.stdin.read().splitlines()
# 本題讀入格式
# ['22  33', '33 1   ', '34 34', '0 0']

for line in lines:
    a, b = (int(i) for i in line.split())
    if a == 0 and b == 0:
        break
    print(a) if a > b else print(b)
