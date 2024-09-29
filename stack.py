# Initialize an empty stack
stack = []


def push(element):
    stack.append(element)
    print("Pushed {} onto the stack".format(element))

def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
    else:
        element = stack.pop()
        print("Popped {} from the stack".format(element))


def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Current stack:", stack)


while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        element = input("Enter element to push onto the stack: ")
        push(element)
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
