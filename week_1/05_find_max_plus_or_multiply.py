input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    max_number = 0
    for element in array:
        plus_number = max_number + element
        multiply_number = max_number * element
        if plus_number > multiply_number:
            max_number = plus_number
        else:
            max_number = multiply_number

    return max_number


result = find_max_plus_or_multiply(input)
print(result)