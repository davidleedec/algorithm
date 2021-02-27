numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    start_list = [0]
    for i in array:
        new_array_list = []
        for s in start_list:
            new_array_list.append(s+i)
            new_array_list.append(s-i)
        start_list = new_array_list
    target_count = start_list.count(target)
    return target_count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!