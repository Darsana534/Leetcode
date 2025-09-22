class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zr, zc = set(), set()
        
        # Step 1: Record rows and columns to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zr.add(i)
                    zc.add(j)
        
        # Step 2: Zero out rows
        for i in zr:
            for j in range(n):
                matrix[i][j] = 0
        
        # Step 3: Zero out columns
        for j in zc:
            for i in range(m):
                matrix[i][j] = 0
