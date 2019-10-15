def palindrome_permutation(input_str):
    value_count = {}
    for i in input_str:
        if i in value_count:
            value_count[i] += 1
        else:
            value_count[i] = 1
    odd_num_count = 0
    for j in value_count.values():
        if j % 2 != 0:
            odd_num_count += 1
    if odd_num_count > 1:
        return False
    else:
        return True




if __name__ == "__main__":
    test_string = "hheehheehheehheehheehheehheeji"
    result = palindrome_permutation(test_string)
    print(result)