import re
def fun(s):
    a = r"^([a-zA-Z0-9_-])+\@([a-zA-Z0-9])+\.([a-zA-Z]){1,3}$"
    return re.match(a, s)

