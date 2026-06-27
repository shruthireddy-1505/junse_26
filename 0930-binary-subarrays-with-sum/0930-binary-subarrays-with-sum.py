class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0:1}
        pref = 0
        count = 0 
        for i in nums:
            pref += i
            if pref - goal in d:
                count += d[pref - goal]
            if pref in d:
                d[pref] += 1
            else:
                d[pref] = 1
        return count
        