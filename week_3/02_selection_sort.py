input = [4, 6, 2, 9, 1]


# -> -> -> -> ->
# [4, 6, 2, 9, 1]
#    -> -> -> ->
# [1, 6, 2, 9, 4]
#       -> -> ->
# [1, 2, 6, 9, 4]

def insertion_sort(array):
    # 이 부분을 채워보세요!

    for i in range(len(array)):
        min_index = i
        for j in range(len(array) - i):
            # print(i+j)
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
