s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    parenthesis = []
    if string[0] == ')':
        return False
    for i in range(len(string)):
        if string[i] == "(":
            parenthesis.append('(')
        else:
            if not len(parenthesis):
                return False
            parenthesis.pop()
    if len(parenthesis) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!

# input = "(())()"
#
#
# def is_correct_parenthesis(string):
#     stack = []
#
#     for i in range(len(string)):
#         if string[i] == "(":
#             stack.append(i)  # 여기 아무런 값이 들어가도 상관없습니다! ( 가 들어가있는지 여부만 저장해둔 거니까요
#         elif string[i] == ")":
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#
#     if len(stack) != 0:
#         return False
#     else:
#         return True
#
#
# print(is_correct_parenthesis(input))  # True 를 반환해야 합니다!