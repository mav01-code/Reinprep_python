def transpose(x):
    return [[x[j][i] for j in range(len(x))]for i in range(len(x[0]))]

def matrix():
    rows, cols= map(int, input().split(", "))
    a=[]
    for i in range(rows):
        row=list(map(int, input().split(", ")))
        a.append(row)
    return a

x=matrix()
res=transpose(x)
for i in res:
    print(", ".join(map(str, i)))