class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next
        return True

    def enqueue(self, value):
        new_node = Node(value)
        

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        
        if self.length > 0:
            temp = self.last
            temp.next = new_node
            temp = temp.next
            self.last = temp

        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = temp.next
        self.length -= 1
        return temp


my_queue = Queue(0)
my_queue.dequeue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()