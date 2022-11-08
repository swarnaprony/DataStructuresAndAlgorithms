class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp.value
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
        self.length -= 1
        return temp
    
    def get(self, index):
        temp = self.head
        if index <0 or index > self.length:
            return None 
        if index == 0:
            return temp
        else: 
            for _ in range(index):
                temp = temp.next
        return temp

    def set_value(self, index, value):
        new_node = Node(value)
        if index == 0 and self.length == 1:
            self.head = new_node
            self.tail = new_node
        if index == (self.length -1):
            temp = self.tail.prev
            temp.next = new_node
            self.tail = temp.next
            return True
        if index == 0 and self.length > 1:
            temp = self.head
            new_node.next = temp.next
            self.head = new_node
            self.length += 1
            return True
        if index > 0 and index < (self.length-1):
            temp = self.head
            next_node = temp.next

            for _ in range(index-1):
                temp = temp.next
                next_node = temp.next
            new_node.next = next_node.next
            temp.next  = new_node
            self.length += 1
            return True


    def insert(self, index, value):
        new_node = Node(value)

        if index == 0 and self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        if index == 0 and self.length > 0:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            self.length += 1
            return True

        if index > 0:
            temp = self.head
            next = temp.next

            for _ in range(index-1):
                prev = temp
                temp = temp.next
                next = temp.next

            new_node.next = next
            temp.next  = new_node
            self.length += 1
            return True
        
        

            


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)


print('DLL before insert():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(1,2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(0,0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(4,4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()


    