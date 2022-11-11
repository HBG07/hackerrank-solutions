if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    c = -101
    d = max(arr)
    e = 0
    for i in arr:
        if(i>c and i<d):
            e=i
            c=i
    print(e)
