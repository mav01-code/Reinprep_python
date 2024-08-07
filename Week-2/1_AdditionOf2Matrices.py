n1=int(input())
m1=[]
for i in range(n1):
    k=[int(i) for i in input().split(",")]
    m1.append(k)
n2=int(input())
m2=[]
for i in range(n2):
    k=[int(i) for i in input().split(",")]
    m2.append(k)
add=[[m1[i][j]+m2[i][j] for j in range(n1)] for i in range(n1)]
for i in add:
    print(*i, sep=", ")