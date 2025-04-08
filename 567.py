# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# # Example 1:

# # Input: s1 = "ab", s2 = "eidbaooo"
# # Output: true
# # Explanation: s2 contains one permutation of s1 ("ba").

# # Example 2:

# # Input: s1 = "ab", s2 = "eidboaoo"
# Output: false




def solution(self, s1, s2):
    return trim(''.join(sorted(s1)), s2)

def trim(s1, s2):
    
    if len(s1) > len(s2):
        return False
    
    
    if (s1 == ''.join(sorted(s2[:len(s1)]))):
        return True
    
    return trim(s1, s2[1:]) 
    
