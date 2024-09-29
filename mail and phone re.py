import re
fin=open("file_name.txt",'r')
lines=fin.read()
regex=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
Nregex=re.compile(r'\+[9][1]\d{1,10}')
match=regex.finditer(lines)
matches=Nregex.finditer(lines)
for i in match:
    print(i.group())
for j in matches:
    print(j.group())
