class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        for i in range(len(nums)):
            mid=len(nums)//2
            if nums[i]==target:
                return i
            if nums[mid]<=target:
                l=mid+1
            if nums[mid]>=target:
                r=mid-1
        return -1