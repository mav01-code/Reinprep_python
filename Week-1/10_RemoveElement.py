nums=list(map(int,input().split(",")))
val=int(input())
a=[]
count=0
for i in nums:
    if i!=val:
        a.append(i)
for i in a:
    count+=1
print(count)