# -------------------------------------------------------------#
# Implementation of a simple stack.
# - This does not use any singly/doubly linked lists implementations
# Shaishav Shah
# 2021-05-01
# -------------------------------------------------------------# 

class Stack:
    def __init__(self):
        self.__items = []
        self.__size = 0

    # Getter Methods
    
    def peek(self):
        if self.__size:
            print("The top item of the stack is {}".format(self.__items[-1]))
        else:
            print("The Stack is empty!")
    
    def isEmpty(self):
        return self.__size == 0

    def size(self):
        return self.__size

    def search(self, item):
        """
        This method searches and returns the position of the item within the stack. Top of stack = position 0. Bottom of stack = position n-1. Not found = -1
        """
        try:
            reversePosition = self.__items.index(item)
        except ValueError:
            return -1
        else:
            return self.__size - reversePosition
    
    # Setter Methods

    def pop(self):
        assert self.__size > 0, "Stack is empty!"
        self.__size -= 1
        return self.__items.pop()
    
    def push(self, item):
        self.__items.append(item)
        self.__size += 1
    

    # Other Methods

    def __str__(self):
        current_str = "Stack (Bottom -> Top): "
        for item in self.__items:
            current_str += " -> {}".format(str(item))
        current_str += "\n"
        return current_str

    def __repr__(self):
        return str(self.__items)
    

if __name__ == "__main__":
    stack = Stack()
    for i in range(1,6):
        stack.push(i)
    print(stack)
    print(stack.search(4))
    stack.pop()
    stack.peek()
    while not stack.isEmpty():
        stack.pop()
    stack.peek()