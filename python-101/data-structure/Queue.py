#%%
from SinglyLinkedList import SinglyLinkedList

class Queue(object):
    firstInstance = SinglyLinkedList()

    def dequeue(self):
        return self.firstInstance.removeAt(0)
    
    def enqueue(self, value):
        self.firstInstance.insertAt(value, self.firstInstance.getSize())

queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())