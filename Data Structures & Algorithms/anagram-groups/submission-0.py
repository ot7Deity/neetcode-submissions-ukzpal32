class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for char in strs:
            key = tuple(sorted(char))
            if key not in groups:
                groups[key] = [char]
            else:
                groups[key].append(char)
        return list(groups.values())
        



        