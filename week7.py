# Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ). Your solution must be recursive.

# Evaluate the time and space complexity of your solution.

def is_nested(paren_s):
    stack = []
    return helper(paren_s, stack)
    

def helper(paren_s, stack):
    
    if (len(paren_s) == 0):
        return len(stack) == 0
    
    if (paren_s[0] == ')'):
        if not stack:
            return False
            
        stack.pop()
    else:
        stack.append(paren_s[0])
    
    return helper(paren_s[1:], stack) #//

print(is_nested("(())"))
    
    
    
    

# Example usage
#))


