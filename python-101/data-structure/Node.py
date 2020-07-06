#%%
class Node:
    nodeNext = ''
    objValue = ''
    binhead = False
    binTail = False

    def __init__(self, objValue = '', nodeNext = '', binHead = False, binTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail

    def getValue(self):
        return self.objValue
    
    def setValue(self, objValue):
        self.objValue = objValue

    def getNext(self):
        return self.nodeNext
    
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    
    def isHead(self):
        return self.binHead
    
    def isTail(self):
        return self.binTail

# node1 = Node(objValue = 'a')
# nodeTail = Node(binTail = True)
# nodeHead = Node(binHead = True, nodeNext = node1)