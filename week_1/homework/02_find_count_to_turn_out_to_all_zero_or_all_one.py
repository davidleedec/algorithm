input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    number_zero = 0
    number_one = 0

    if string[0] == "0":
        number_one = 1
    else:
        number_zero = 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            if string[i] == "0":
                number_one += 1
            else:
                number_zero += 1

    if number_zero < number_one:
        return number_zero
    else:
        return number_one


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
