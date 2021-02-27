input = 100

def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = [2]
    for n in range(2, number+1):
        for p in prime_list:
            if n % p == 0:
                break
            if p > n/p:
                prime_list.append(n)
                break

    return [prime_list]


result = find_prime_list_under_number(input)
print(result)