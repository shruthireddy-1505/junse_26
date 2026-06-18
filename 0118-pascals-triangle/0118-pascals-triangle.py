class Solution:
    def generate(self, n: int) -> List[List[int]]:
        mat = [[0]*(i+1) for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if j == 0 or j == i :
                    mat[i][j] = 1
                else:
                    ans = mat[i-1][j-1] + mat[i-1][j]
                    mat[i][j] = ans
                
        return mat

        