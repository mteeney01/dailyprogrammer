import math

inputs = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [3, 5, 7, 8, 1, 6, 4, 9, 2],
    [8, 1, 6, 7, 5, 3, 4, 9, 2, 3, 4, 5, 6, 5, 6, 7],
    [8,58,59,5,4,62,63,1,49,15,14,52,53,11,10,56,41,23,22,44,45,19,18,48,32,34,35,29,28,38,39,25,40,26,27,37,36,30,31,33,17,47,46,20,21,43,42,24,9,55,54,12,13,51,50,16,64,2,3,61,60,6,7,57]
]


def magic_squares(square):
    row_size = math.sqrt(len(square))
    if row_size.is_integer():
        return check_sum(square, int(row_size))
    else:
        return False

def check_sum(square, row_size):
    rows =  [square[i:i+row_size] for i in range(0, len(square), row_size)]
    cols =  [square[i::row_size] for i in range(0, row_size)]
    topLeftDiag = [square[i+row_size*i] for i in range(0, row_size)]
    bottomLeftDiag = [square[row_size*i+(row_size-i-1)] for i in range(0, row_size)]

    total = sum(rows[0])

    rows_match = all([total == sum(r) for r in rows])
    cols_match = all([total == sum(c) for c in cols])
    firstDiagMatch = total == sum(topLeftDiag)
    secondDiagMatch = total == sum(bottomLeftDiag)

    return rows_match and cols_match and firstDiagMatch and secondDiagMatch


for input in inputs:
    print(magic_squares(input))