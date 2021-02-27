from itertools import zip_longest

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    max_discounted_price = 0

    for i, (price, coupon) in enumerate(zip_longest(prices, coupons)):
        if coupon is None:
            max_discounted_price += price
        else:
            max_discounted_price += price * (1 - (coupon / 100))

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
