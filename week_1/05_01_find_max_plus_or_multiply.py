input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    max_number = 0
    for number in array:
        if number <= 1 or max_number <= 1:
            max_number += number
        else:
            max_number *= number
    return max_number


result = find_max_plus_or_multiply(input)
print(result)