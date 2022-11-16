def average(array):
    avg = 0
    for i in set(array):
        avg+=i
    return avg/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
