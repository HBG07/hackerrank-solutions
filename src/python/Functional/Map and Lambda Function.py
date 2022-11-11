cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    l = []
    one = 1
    second = 0
    actual = 0
    for i in range(n):
        l.append(actual)
        actual = one + second
        one = second
        second = actual
    return l
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))