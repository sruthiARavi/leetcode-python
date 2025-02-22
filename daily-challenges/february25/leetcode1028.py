"""
# 1028. Recover a Tree From Preorder Traversal
# We run a preorder depth-first search (DFS) on the root of a binary tree.
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  
# If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
# If a node has only one child, that child is guaranteed to be the left child.
# Given the output traversal of this traversal, recover the tree and return its root.
"""

"""
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
"""

class leetcode1028(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        if not traversal or traversal is None:
            # Input conditions render this moot but it's good practice to add this check anyway
            return 
        
        stack = []
        index = 0
        while index < len(traversal):
            """
             # 1. Count the number of dashes
             # 2. Extract the value
             # 3. Create the current node
             # 4. Adjust the stack depth
             # 5. Attach the current node to its parent
             # 6. Push the current node onto the stack
            """

            # 1. Count the number of dashes
            curr_depth = 0
            while index < len(traversal) and traversal[index] == "-":
                curr_depth += 1
                index += 1
            
            # 2. Extract the value
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            
            # 3. Create the current node
            node = TreeNode(value)

            # 4. Adjust the stack depth
            while(len(stack) > curr_depth):
                stack.pop()

            # 5. Attach the current node to its parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            # 6. Push the current node onto the stack
            stack.append(node)       
        
        return stack[0]                    
