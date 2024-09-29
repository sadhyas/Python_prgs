class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

s=stack()
print("MENU DRIVEN STACK PROGRAM")
while True:
    print("1:push\n 2:pop\n 3:size\n 4:display\n 5:exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        val=input("enter the value to be pushed:")
        s.push(val)
    elif choice==2:
        if s.items==[]:
            print("stack is empty")
        else:
            print("deleted item:",s.pop())
    elif choice==3:
        print("size of stack is: ",s.size())
    elif choice==4:
        if s.items==[]:
            print("stack is empty")
        else:
            print("stack items are :\n",s.items)
    elif choice==5:
        print("thankyou")
        exit(0)
    else:
        print("invalid choice")

    
    
