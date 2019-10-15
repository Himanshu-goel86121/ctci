def one_away(input_str1, input_str2):
    big_str = ""
    small_str = ""
    if len(input_str1) >= len(input_str2):
        big_str = input_str1
        small_str = input_str2
    else:
        big_str = input_str2
        small_str = input_str1
    if len(big_str) - len(small_str) > 1:
        return False
    elif len(big_str) - len(small_str) == 0:
        replace_count = 0
        for i in range(len(big_str)):
            if big_str[i] != small_str[i]:
                if replace_count >= 1:
                    return False
                replace_count +=1
        if replace_count <= 1:
            return True
        else:
            return False

    else:
        insert_edit_count = 0
        j = 0
        for i in range(len(big_str)):
            if j == len(small_str):
                return True
            if big_str[i] != small_str[j]:
                if insert_edit_count >= 1:
                    return False
                insert_edit_count += 1
            else:
                j += 1
        if insert_edit_count <= 1:
            return True
        else:
            return False


if __name__ == "__main__":
    test_string1 = "pale"
    test_string2 = "bake"
    result = one_away(test_string1, test_string2)
    print(result)