# Find the element repeated the most number of times
def majority(nums):
    count=0
    temp=None
    for i in nums:
        if count==0:
            temp=i
        count+=(1 if i==temp else -1)
    return temp
nums=list(map(int, input().split(",")))
print(majority(nums))