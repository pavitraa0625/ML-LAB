def multiply_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(A, m):
    result = A
    for _ in range(m - 1):
        result = multiply_matrices(result, A)
    return result

n = int(input("Enter size of square matrix (n x n): "))

print("Enter the matrix row by row:")
A = []
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    A.append(row)

m = int(input("Enter the power m: "))


result = matrix_power(A, m)


print(f"\nMatrix A^{m} is:")
for row in result:
    print(row)
