class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
        print (new_data,'has been added to the front of the list')

    def append(self, new_data):
        current = self.head
        newNode = Node(new_data)
        newNode.next = None

        if self.head is None:
            self.head = newNode
            return
            
        while (current.next):
            current = current.next

        current.next = newNode
        print (new_data,'has been added to the end of the list')

    def delete(self, data):
        temp = self.head
        if (temp is None):
            print ('list already empty')
            return

        prev = None

        while (temp is not None and temp.data is not data):
            prev = temp
            temp = temp.next

        if (temp is None):
            print ('list does not contain the value', data)
            return

        prev.next = temp.next

    def reverse(self):
        prev = None
        current = self.head
        nextNode = None
        while (current is not None):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        self.head = prev

        print('List is now in reverse order')
            


if __name__=='__main__':

    linkedlist = LinkedList()

    linkedlist.push(7)
    linkedlist.push(5)
    linkedlist.push(8)
    linkedlist.append(76)
    linkedlist.append(57)
    linkedlist.append(5763)
    linkedlist.push(45)
    linkedlist.push(786576)
    linkedlist.append(3456)
    
    linkedlist.delete(45)
    linkedlist.delete(63)
    linkedlist.printlist()

    linkedlist.reverse()
    linkedlist.printlist()
