class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        for char in nums:
            if char in seen:
                return char
            else:
                seen.add(char)
        
        