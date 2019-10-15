def check_permutations(str1, str2):
    temp_dict = {}
    assert len(str1) == len(str2)
    for character in str1:
        if character in temp_dict.keys():
            temp_dict[character] += 1
        else:
            temp_dict[character] = 1

    for character in str2:
        if character not in temp_dict.keys():
            return False
        else:
            temp_dict[character] -= 1
    for count in temp_dict.values():
        if count != 0:
            return False
    return True


if __name__ == "__main__":
    test_string1 = "her"
    test_string2 = "reh"
    print(check_permutations(test_string1, test_string2))
