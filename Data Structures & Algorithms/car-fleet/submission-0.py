class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up positions and speeds
        pairs=(list(zip(position,speed)))

        # Sort by position (which direction?)
        sorted_pairs_in_reverse=sorted(pairs, key=lambda x:x[0], reverse=True )
        stack=[]
        for pos, spd in sorted_pairs_in_reverse:
            time = (target-pos)/spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


