uppercase,lowercase,words,digits=0,0,0,0
str=input("enter a sentence")
for i in str:
    if i.islower():
        lowercase+=1
    elif i.isupper():
        uppercase+=1
    elif i.isdigit():
        digits+=1
words=len(str.split())
print("uppercase:",uppercase)
print("lowercase:",lowercase)
print("digits:",digits)
print("words:",words)
