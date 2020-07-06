#%%
from SinglyLinkedList import SinglyLinkedList

class Stack(object):
    
    lstInstance = SinglyLinkedList()

    def pop(self):
        return self.lstInstance.removeAt(0)
    
    def push(self, value):
        self.lstInstance.insertAt(value, 0)

# stack = Stack()
# stack.push('a')
# stack.push('b')
# stack.push('c')

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())