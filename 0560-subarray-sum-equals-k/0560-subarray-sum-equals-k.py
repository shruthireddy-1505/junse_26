class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = 0
        count = 0
        d = {0:1}
        for i in range(n):
            pref += nums[i]
            if pref - k in d:
                count += d[pref-k]
            if pref in d:
                d[pref] += 1
            else:
                d[pref] = 1
        return count


        