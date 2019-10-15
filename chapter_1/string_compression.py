def string_compression(input_string):
    current_character = input_string[0]
    current_count = 1
    new_str_list = []
    for i in range(1, len(input_string)):
        if input_string[i] == current_character:
            current_count += 1
        else:
            new_str_list.append(current_character)
            new_str_list.append(str(current_count))
            current_character = input_string[i]
            current_count = 1
    new_str_list.append(current_character)
    new_str_list.append(str(current_count))
    new_str = "".join(new_str_list)
    if len(new_str) >= len(input_string):
        return input_string
    else:
        return new_str



if __name__ == "__main__":
    test_string = "aabaabaabaabbbbbb"
    result = string_compression(test_string)
    print(result)