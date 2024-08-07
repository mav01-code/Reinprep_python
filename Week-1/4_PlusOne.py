nums = list(map(int,input().split(", ")))
s=''
for i in nums:
    s+=str(i)
t=int(s)+1
a=[]
for i in str(t):
    a.append(int(i))
print(*a, sep=', ')
