def is_unique(input_string):
    temp_dict = {}
    for character in input_string:
        if character in temp_dict.keys():
            return False
        else:
            temp_dict[character] = True
    return True


if __name__ == "__main__":
    test_string = "himanshu"
    print(is_unique(test_string))
