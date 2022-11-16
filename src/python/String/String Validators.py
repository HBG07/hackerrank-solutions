if __name__ == '__main__':
    s = input()

    a, b, c, d, e = False, False, False, False, False
    for i in s:
        a, b, c, d, e = a or i.isalnum(), b or i.isalpha(), c or i.isdigit(), d or i.islower(), e or i.isupper()
    print(str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d)+'\n'+str(e))
