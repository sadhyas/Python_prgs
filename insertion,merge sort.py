def insertionsort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
def mergesort(arr):
    R=L=[]
    if len(arr)>1:
        mid=len(arr)//2
        R=arr[mid:]
        L=arr[:mid]
        mergesort(L)
        mergesort(R)
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1
def printlist(arr):
    for i in range (len(arr)):
        print(arr[i],end="")
    print()

while(True):
    print("1:insertion sort")
    print("2:merge sort")
    ch=int(input("enter your choice:"))
    if ch==1:
        arr=list(map(int,input("enter the elements:").strip().split()))
        print(arr)
        insertionsort(arr)
        printlist(arr)
    elif ch==2:
        arr=list(map(int,input("enter the elements:").strip().split()))
        print(arr)
        mergesort(arr)
        printlist(arr)
    else:
        exit(1)

    
        
        
    
