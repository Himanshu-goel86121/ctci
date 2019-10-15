def longest_palindrome(input_str):
    odd_palindromes = []
    min_odd_pad = 1
    for i in range(len(input_str)):
        odd_palindromes.append(input_str[i])
        if i - min_odd_pad < 0 or i + min_odd_pad >= len(input_str) or input_str[i - min_odd_pad] != input_str[i + min_odd_pad]:
            continue
        for j in range(1, len(input_str)):
            if i - j < 0:
                break
            if i + j >= len(input_str):
                break
            if input_str[i - j] == input_str[i + j]:
                odd_palindromes.append(input_str[i - j: i + j + 1])
                min_odd_pad = j + 1
            else:
                break
    even_palindromes = []
    min_even_pad = 1
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            even_palindromes.append(input_str[i: i + 2])
        else:
            continue
        if i - min_even_pad < 0 or i + min_even_pad >= len(input_str) or input_str[i - min_even_pad] != input_str[i + min_even_pad + 1]:
            continue
        for j in range(1, len(input_str)):
            if i - j < 0:
                break
            if i + j + 1 >= len(input_str):
                break
            if input_str[i - j] == input_str[i + j + 1]:
                even_palindromes.append(input_str[i - j: i + j + 2])
                min_even_pad = j + 1
            else:
                break
    if min_even_pad >= min_odd_pad and len(even_palindromes) > 0:
        palindrome_len = 2 * (min_even_pad - 1) + 2
        for palindrome in even_palindromes:
            if len(palindrome) == palindrome_len:
                return palindrome
    else:
        palindrome_len = 2 * (min_odd_pad - 1) + 1
        for palindrome in odd_palindromes:
            if len(palindrome) == palindrome_len:
                return palindrome



if __name__ == "__main__":
    test_string = "himanshuadaauhsramesh"
    print(longest_palindrome(test_string))