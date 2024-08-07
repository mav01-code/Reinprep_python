open = ["{", "[", "("]
close = ["}", "]", ")"]
def check(s):
    stack=[]
    for i in s:
        if i in open:
            stack.append(i)
        elif i in close:
            pos=close.index(i)
            if len(stack)>0 and open[pos]==stack[len(stack)-1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"
s=input()
print(check(s))