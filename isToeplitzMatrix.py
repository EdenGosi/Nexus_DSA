class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(
            matrix[r][c] == matrix[r + 1][c + 1]
            for r in range(len(matrix) - 1)
            for c in range(len(matrix[0]) - 1)
        )
