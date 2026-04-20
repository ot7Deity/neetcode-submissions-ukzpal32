class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator={"+":lambda a, b: a+b, "-":lambda a, b: a - b,"*":lambda a, b: a * b,"/":lambda a, b: int(a / b) }
        stack=[]
        for char in tokens:
            if char not in operator:
                stack.append(int(char))
            else:
                a=stack.pop()
                b=stack.pop()
                stack.append(operator[char](b,a))
        return stack[0]
            

        