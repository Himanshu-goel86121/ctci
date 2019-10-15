def URLify(url, length):
    spaces = len(url[length:])
    url = [character for character in url]
    min_iter_val = spaces - 1
    i = len(url) - 1
    space_replacement = ["0", "2", "%"]
    while(i >= spaces):
        if url[i - spaces] != " ":
            url[i] = url[i - spaces]
            i -= 1
        else:
            for j in range(3):
                url[i] = space_replacement[j]
                i = i - 1
            spaces -= 2
    print(url)



if __name__ == "__main__":
    test_url = "Mr John Smith    "
    test_length = 13
    URLify(test_url, test_length)
