class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def work(k):
            hour=0
            for p in piles:
                hour+=math.ceil(p/k)
            return hour <=h
        l,r=1, max(piles)
        while l< r:
            k= (l+r)//2
            if work(k):
                r=k
            else:
                l=k+1
        return l
        
            
