class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def fun(s):
            if s == "":
                return 1
            if s[0] == "0":
                return 0
            if s in memo:
                return memo[s]
            ways = fun(s[1:])

            if len(s)>=2 and int(s[:2])<=26:
                ways += fun(s[2:])
            memo[s] = ways
            return memo[s]
        return fun(s)

            