class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        # if len(s) == len (t):
        #     for i in s_sorted: 
        #         if i not in t_sorted: 
        #             return False
        # else: 
        #     return False                             
        
        # return True
        if len(s) != len (t):
            return False

        return s_sorted == t_sorted
                
            
