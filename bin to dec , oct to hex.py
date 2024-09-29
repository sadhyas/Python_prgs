import sys
def numtodec(num_val,n,d):
    decval=0
    count=0
    digit=0
    l=len(str(num_val))
    digit=num_val%10
    while (num_val!=0 and digit<=d):
        decval=decval+digit*pow(n,count)
        num_val=num_val//10
        digit=num_val%10
        count+=1
    if (count==l):
        return decval
    else:
        print("invalid input")
def octaltohex(num_val):
    rem=num_val%16
    ch=""
    if(rem<10):
        ch=rem
    if(rem==10):
        ch="A"
    if(rem==11):
        ch="B"
    if(rem==12):
        ch="C"
    if(rem==13):
        ch="D"
    if(rem==14):
        ch="E"
    if(rem==15):
        ch="F"
    if(num_val-rem!=0):
        return octaltohex(num_val//16)+str(ch)
    else:
        return str(ch)

while True:
    print("1: binary to decimal\n2: octal to hexadecimal\n3: exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        num_val=int(input("enter the binary value:"))
        print("binary equivalent is:", numtodec(num_val,2,1))
    elif ch==2:
        num_val=int(input("enter the octal value:"))
        octalno=numtodec(num_val,8,7)
        if (octalno!=None):
            print("hexadecimal is:", octaltohex(octalno))
        else:
            print("cannot be coverted")
    else:
        print("thankyou")
        sys.exit()


    
