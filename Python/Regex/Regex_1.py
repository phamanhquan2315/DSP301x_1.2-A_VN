import re

x = 'My 2 favorite numbers are 98 and 34'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[UEOAI]+',x)
print(y)
