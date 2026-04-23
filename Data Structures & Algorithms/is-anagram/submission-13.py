class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        need,have={},{}
        for c in s:
            need[c]= 1+ need.get(c,0)
        for c in t:
            have[c]=1 + have.get(c,0)
        if have!=need:
            return False
        else:
            return True
        
       