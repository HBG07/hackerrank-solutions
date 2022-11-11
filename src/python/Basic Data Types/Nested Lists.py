if __name__ == '__main__':
    l = []
    lv = set()
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        l.append([score,name])
        lv.add(score)
    l.sort()
    lv.remove(min(lv))
    val = min(lv)
    for i,j in l: 
        if(i==val):
            print(j)