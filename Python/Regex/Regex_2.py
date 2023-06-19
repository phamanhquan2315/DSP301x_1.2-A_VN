import re

x = 'From : Using the : characters'
y = re.findall('^F.+?:',x)
print(y)

x = 'From stephen.marquard@utc.ac.za Sat Jun 5 09:12:16 2023'
y = re.findall('\S+@\S+',x)
print(y)

y = re.findall('^From (\S+@\S+)',x)
print(y)

atpos = x.find('@')
sppos = x.find(' ',atpos)

print(x[atpos:sppos])

y= re.findall('^From .*@([^ ]*)',x)
print(y)