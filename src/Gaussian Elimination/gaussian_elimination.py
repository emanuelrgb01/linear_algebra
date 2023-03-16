import numpy as np


def back_substitution(A, b):
    for line in range(len(A)-1, -1, -1):
        if abs(A[line][line]) < 1e-12:
            print("Error")
            return
        S = 0
        for column in range(line+1, len(A), 1):
            S = S + A[line][column]*b[column]
        b[line] = (b[line] - S)/A[line][line]

    return b


def gaussian_elimination(A, b):
    n = len(A)-1
    for step in range(0, n, 1):
        if abs(A[step][step]) < 1e-12:
            print("Error")
            return
        for line in range(step+1, n+1, 1):
            m = A[line][step]/A[step][step]
            A[line][step] = 0
            b[line] = b[line] - m*b[step]
            for column in range(step+1, n+1, 1):
                A[line][column] = A[line][column] - m*A[step][column]

    return back_substitution(A, b)


# Example
if __name__ == '__main__':
    A = np.array([[2, 1, 1],
                  [4, 3, 3],
                  [8, 7, 9]], np.float64)

    b = np.array([[1],
                  [2],
                  [6]], np.float64)
    print(f'x = {gaussian_elimination(A, b)}')
