import re
a = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]',input(),re.I)
print('\n'.join(a or ['-1']))