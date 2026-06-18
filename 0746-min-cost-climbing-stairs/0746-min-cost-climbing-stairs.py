class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        def fun(cost,i):
            if i >= len(cost):
                return 0
            if i in d:
                return d[i]
            fun1 = fun(cost,i+1)
            fun2 = fun(cost,i+2)
            d[i] =  cost[i] + min(fun1,fun2)
            return d[i]

        return min(fun(cost,0),fun(cost,1))