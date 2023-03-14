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


# Example
if __name__ == '__main__':
    A = np.array([[2, 1, 1],
                  [0, 1, 1],
                  [0, 0, 2]], np.float64)

    b = np.array([[1],
                  [0],
                  [2]], np.float64)

    print(f'x = {back_substitution(A, b)}')
