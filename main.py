def diagonal_sum(matrix):
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        return "Matrix not square"
    
    n = len(matrix)
    primary_diagonal_sum = sum(matrix[i][i] for i in range(n))
    secondary_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))
    
    if n % 2 == 1:
        return primary_diagonal_sum
    else:
        return primary_diagonal_sum + secondary_diagonal_sum

# Misol uchun matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(matrix))  # 30
