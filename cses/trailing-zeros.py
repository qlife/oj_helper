n = int(input())
# less than 10**9
m = [5 ** i for i in range(1, 13)]
s = sum([n // x for x in m])
print(s)
