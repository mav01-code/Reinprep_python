def richest(accounts):
    max=0
    for i in range(len(accounts)):
        count=0
        for j in range(len(accounts[i])):
            count+=account[i][j]
        if count>max:
            max=count
    return max

account=[]
n=int(input())
for i in range(n):
    k=[int(i) for i in input().split(",")]
    account.append(k)
print(richest(account))