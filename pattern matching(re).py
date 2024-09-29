import re
text_search='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 hi this is python lab .&^*()+_[]\()| 123-456-7890 999-777-4444 abc-23b-7890 123-567-345 123.456.7890 welcome to acharya bangalore'''
pattern=re.compile(r'\d{1,3}\-\d{1,3}\-\d{1,4}')
matches=pattern.finditer(text_search)
print("using regular expression:")
for match in matches:
    print(match.group())
def isphonenumber():
    ss=text_search.split()
    pat_mat=list()
    for i in ss:
        if len(i)==12 and i[3]=='-' and i[7]=='-':
            pat_mat.append(i)
    for i in pat_mat:
        trans=i.translate({ord('-'):None})
        if trans.isdigit():
            print(i)
print("without using regular exp:")
isphonenumber()
