def mul(x,y):
    return [[sum(x[i][k]*y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]

def matrix():
    rows, cols = map(int, input().split(", "))
    a=[]
    for i in range(rows):
        row = list(map(int, input().split(", ")))
        a.append(row)
    return a

x = matrix()
y = matrix()
res = mul(x,y)

for i in res:
    print(", ".join(map(str, i)))
