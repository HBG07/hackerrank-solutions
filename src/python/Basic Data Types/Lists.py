myList = []

def op(string):
    if string[0] == 'insert':
        myList.insert(int(string[1]),int(string[2]))
    elif string[0] == 'remove':
        myList.remove(int(string[1]))
    elif string[0] == 'append':
        myList.append(int(string[1]))
    elif string[0] == 'sort':
        myList.sort()
    elif string[0] == 'reverse':
        myList.reverse()
    elif string[0] == 'pop':
        myList.pop()
    else:
        print(myList)
    
if __name__ == '__main__':
    N = int(raw_input())
    while N:
        a = raw_input().split(' ')
        op(a)
        N-=1
