class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        for a,b in zip(s,t):
            s_count[a] = s_count.get(a, 0) + 1
            t_count[b] = t_count.get(b, 0) + 1
        
        for key,value in t_count.items():
            if s_count.get(key) != value:
                return False

        return True