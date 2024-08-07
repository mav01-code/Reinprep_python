nums = list(map(int,input().split(",")))
a = []
n=0
for i in nums:
    n+=i
    a.append(n)
print(*a, sep=", ")