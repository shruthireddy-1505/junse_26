class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(nums,ind,ans):
            if ind >= len(nums):
                res.append(ans[:])
                return
            ans.append(nums[ind])
            solve(nums,ind+1,ans)

            ans.pop()
            solve(nums,ind+1,ans)

        solve(nums,0,[])
        return res

        