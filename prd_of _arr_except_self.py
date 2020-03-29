lst = [1, 2, 3, 4, 5]


def prd_of_arr_exp_self(arr):
    output = []
    for i, e in enumerate(arr):
        output.append(1)
        for j in range(i + 1, len(arr)):
            output[i] *= arr[j]
        for j in range(i - 1, 0, -1):
            output[i] *= arr[j]
    return output


print(prd_of_arr_exp_self(lst))
