class A:
    def __init__(self,s):
        self.s = s

    def palindrome (self):
        rev = self.s[::-1]
        if (rev == self.s):
            print("The string is palindrome:")
        else:
            print("The string is not a palindrome:")

class B (A):
    def palindrome (self):
        rev=0
        count=0
        temp=self.s
        while (self.s!=0):
            dig=self.s%10
            rev=rev*10+dig
            self.s=self.s//10
        if (temp==rev):
            print ("The number is a palindrome!")
        else:
            print("The number isn't a palindrome!")

a = A (input("enter the string:"))
b = B(int (input("enter the integer:")))
a.palindrome ()
b. palindrome ()
