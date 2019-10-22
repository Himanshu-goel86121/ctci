import math


def shortest_palindrome(input_str):
    center = -1
    for i in range(math.ceil(len(input_str) / 2) - 1, -1, -1):
        flag = True
        for j in range(1, i + 1):
            if input_str[i - j] != input_str[i + j]:
                flag = False
        if flag:
            center = i
            break
    for i in range(math.ceil(len(input_str) / 2) - 1, center - 1, -1):
        if input_str[i] != input_str[i + 1]:
            continue
        flag = True
        for j in range(1, i + 1):
            if i + j + 1 >= len(input_str):
                flag = False
                break
            if input_str[i - j] != input_str[i + j + 1]:
                flag = False
        if flag:
            center = i + 0.5
    return input_str[int(center * 2 + 1):][::-1] + input_str


if __name__ == "__main__":
    test_str = "bbbaaaaaabb"
    result = shortest_palindrome(test_str)
    print(result)
