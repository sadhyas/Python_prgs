num1=[]
for i in range (1,100):
    num1.append(i)
print("numbers from 1 to 100 are:\n",num1)
for j,i in enumerate(num1):
    if(i%2!=0):
        del num1[j]
print("the values after deleting odd numbers are:\n",num1)
