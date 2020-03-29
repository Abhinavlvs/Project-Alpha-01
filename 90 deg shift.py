m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


def shift_90_deg(matrix):
    m_90_deg = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[j][i])
        m_90_deg.append(temp)
    return m_90_deg


print(shift_90_deg(m))

# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]