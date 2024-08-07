rows, cols = map(int, input().split(", "))
a=[]
for i in range(rows):
    row = list(map(int, input().split(", ")))
    a.append(row)
    prod=1
for i in range(rows):
    for j in range(cols):
        prod*=a[i][j]
print(prod)