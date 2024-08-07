def postfix(s):
    stack=[]
    op=set(["+", "-", "*", "/"])
    for i in s.split():
        if i not in op:
            stack.append(int(i))
        else:
            op2=stack.pop()
            op1=stack.pop()
            if i=="+":
                stack.append(op1+op2)
            elif i=="-":
                stack.append(op1-op2)
            elif i=="*":
                stack.append(op1*op2)
            elif i=="/":
                stack.append(op1/op2)
    return stack.pop()
s=input()
print(postfix(s))