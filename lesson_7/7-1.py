class Matrix:

    def __init__(self, param_1):
        self.list = param_1

    def __add__(self, other):
        new_m = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                new_m[i][j] = self.list[i][j] + other.list[i][j]
        return new_m

    def __str__(self):
        return f"Результат матрицы: ({self.list})"


m = Matrix([
    [31, 22, 20],
    [5, 7, 9],
    [2, 2, 8]
])
m_2 = Matrix([[2, 4, 6], [5, 4, 3], [1, 3, 6]])


print(f"1 матрица {m}")
print(f"2 матрица {m_2}")

print(f"результат сложения матриц {m.__add__(m_2)}")
