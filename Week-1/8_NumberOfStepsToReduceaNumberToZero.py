n=int(input())
steps=0
while(n):
    if n%2==0:
        steps+=1
        n/=2
    else:
        steps+=1
        n=n-1
print(steps)