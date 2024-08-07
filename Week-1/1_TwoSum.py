def twoSum(nums,target):
    ts={}
    for index, value in enumerate(nums):
        complement = target-value
        if complement in ts:
            return [ts[complement],index]
        ts[value] = index

nums = list(map(int,input().split(",")))
target=int(input())
res=twoSum(nums,target)
print(*res)