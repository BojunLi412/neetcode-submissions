class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = sorted(s)
        t_set = sorted(t)
        if s_sort == t_set:
            return True
        else:
            return False
        
        