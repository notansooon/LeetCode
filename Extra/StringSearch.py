def find_value(names, val):
    left = 0
    right = len(names) -    1
    while (right <= left):
        mid = left + (right - left) / 2
        
        if (names[mid] == val):
            return mid
        elif(val < names[mid]):
            left = mid + 1
        else:
           right = mid - 1
    return -1




# Domain


#!/bin/python3

import math
import os
import random
import re
import sys
import ast



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#
# Complete the 'insert_node' function below.
#
# The function is expected to return a TreeNode.
# The function accepts following parameters:
#  1. TreeNode root
#  2. INTEGER val
#

def remove_node(root, value):
    
    
    if root is None:
        return root  

    
    if val < root.val:
        remove_node(root.left, val)  
    elif val > root.val:
        remove_node(root.right, val)  
    else:
        
        if not root.left and not root.right:
            return None  
    

def sum_tree(root):
    
    if (root is None):
        return root
    
    
    
    return root.val + sum_tree(root.left) + sum_tree(root.right)
    


