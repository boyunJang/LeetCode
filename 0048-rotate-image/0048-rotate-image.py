import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m_len = len(matrix)
        copy_matrix = np.full((m_len, m_len), -1001)
        for y in range(m_len):
            for x in range(m_len):
                copy_matrix[y][x] = matrix[y][x]
        for y in range(m_len):
            for x in range(m_len):
                matrix[y][x] = copy_matrix[m_len - x - 1][y]