input = [4, 6, 2, 9, 1]

#   <-
# [4, 6, 2, 9, 1]
#   <- <-
# [4, 6, 2, 9, 1]
#   <- <- <-
# [4, 6, 2, 9, 1]

def insertion_sort(array):
    # 이 부분을 채워보세요!
    for i in range(1, len(array)): #내코드
        for j in range(i, 0, -1):
            # print(j)
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break
    # n = len(array)  # 스파르타 코팅 코드
    # for i in range(1, n):
    #     for j in range(i):
    #         if array[i - j - 1] > array[i - j]:
    #             array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
    #         else:
    #             break


    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!