class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        pref = 0
        d = {0:-1}
        max_s = 0
        for i in range(n):
            pref += nums[i]
            if pref in d:
                max_s = max(max_s,i-d[pref])
            else:
                d[pref] = i
        return max_s


        