fin=open("text.txt",'r')
lines=fin.readlines()
for i in lines:
    l=i.split()
    for j in l:
        print(j,end='#')
fin.close()

