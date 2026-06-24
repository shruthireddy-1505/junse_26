class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0]*len(nums)
        pref[0] = nums[0]
        for i in range(1,len(nums)):
            pref[i] = pref[i-1] + nums[i]
        for i in range(0,len(nums)):
            left_sum = 0
            right_sum = 0
            if i == 0:
                right_sum = pref[len(nums)-1] - pref[0]
                if left_sum == right_sum:
                    return i
            else:
                left_sum = pref[i-1] 
                right_sum = pref[len(nums)-1] - pref[i]
                if left_sum == right_sum:
                    return i
        return -1
        