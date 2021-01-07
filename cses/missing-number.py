n = int(input())
s0 = sum(map(int, input().split()))
s1 = n * (n+1) // 2
print(s1-s0)