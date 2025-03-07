"""
 # 150. Evaluate Reverse Polish Notation
 # You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
 # Evaluate the expression. Return an integer that represents the value of the expression.
 # Note that:
   ## The valid operators are '+', '-', '*', and '/'.
   ## Each operand may be an integer or another expression.
   ## The division between two integers always truncates toward zero.
   ## There will not be any division by zero.
   ## The input represents a valid arithmetic expression in a reverse polish notation.
   ## The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""
class leetcode150(object):
    def __init__(self, name):
        self.name = name
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "+" : lambda a, b : a + b, 
            "-" : lambda a, b : a - b, 
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(float(a) / b)
          """
          Reminder: 
            - It is good to know that the results of division in python2 will be rounded DOWN to an integer. 
            - So int(6 / (-132)) would be -1. so we should push floated number into the stack and it works like int(6.0 / (-132)) would be 0. 
            - At the end we take the int() of the final result as the output.
          """
        }

        stack = []
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = operations[token]               
                stack.append(operation(num1, num2))
            else:
                stack.append(int(token))

        return stack.pop()
        
