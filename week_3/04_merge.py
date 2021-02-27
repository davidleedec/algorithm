array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    # 이 부분을 채워보세요!
    result = []
    a1 = 0
    a2 = 0
    while a1 < len(array1) and a2 < len(array2):
        if array1[a1] < array2[a2]:
            result.append(array1[a1])
            a1 += 1
        else:
            result.append(array2[a2])
            a2 += 1
    if a1 == len(array1):
        while a2 < len(array2):
            result.append(array2[a2])
            a2 += 1

    if a2 == len(array2):
        while a2 < len(array2):
            result.append(array1[a1])
            a1 += 1




    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!