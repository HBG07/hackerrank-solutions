def count_substring(string, sub_string):
    x = 0
    count = 0
    while string.find(sub_string, x) != -1:
        count += 1
        x = string.index(sub_string, x)+1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
