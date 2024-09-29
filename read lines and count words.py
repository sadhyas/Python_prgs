file_name = input ("enter the file name:")

fin = open(file_name,'r')

n=int(input("enter the no of lines to read:"))

for i in range (n) :
    line=fin.readline()
    print(line)

word=input ("enter the word to count occurrence:")
fin.seek(0)

fwords = fin.read()

print("no. of words are:", fwords.count(word))

fin.close()
