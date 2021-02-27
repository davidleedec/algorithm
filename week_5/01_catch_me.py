from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0

    while 1:
        cony_loc += time

        # ???? 이 셋 중 뭘로 해야 할까요?
        new_position = brown_loc - 1
        new_position = brown_loc + 1
        new_position = brown_loc * 2

        time += 1


print(catch_me(c, b))