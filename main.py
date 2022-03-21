main.py
n = int(input())
res = {input() for _ in range(int(input()))}
for _ in range(n - 1):
    res &= {input() for _ in range(int(input()))}

print(*sorted(res), sep='\n')