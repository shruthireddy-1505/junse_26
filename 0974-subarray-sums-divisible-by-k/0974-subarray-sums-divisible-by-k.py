class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        pref = 0
        d = {0:1}
        for i in nums:
            pref += i
            if pref%k in d:
                count += d[pref%k]
            if pref%k in d:
                d[pref%k] += 1
            else:
                d[pref%k] = 1
        return count

        