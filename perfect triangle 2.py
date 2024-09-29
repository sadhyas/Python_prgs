side1=int(input("enter side1:"))
side2=int(input("enter side2:"))
side3=int(input("enter side3:"))

if side1%3==0:
    if side2%4==0 and side3%5==0:
        print("it is a perfect triangle")
    elif side2%5==0 and side3%4==0:
        print("it is a perfect triangle")
    else:
        print("not a perfect triangle")
        
elif side1%4==0:
    if side2%3==0 and side3%5==0:
        print("it is a perfect triangle")
    elif side2%5==0 and side3%3==0:
        print("it is a perfect triangle")
    else:
        print("not a perfect triangle")

elif side1%5==0:
    if side2%3==0 and side3%4==0:
        print("it is a perfect triangle")
    elif side2%4==0 and side3%3==0:
        print("it is a perfect triangle")
    else:
        print("not a perfect triangle")

else:
     print("not a perfect triangle")

    
    
    
        
    

    
