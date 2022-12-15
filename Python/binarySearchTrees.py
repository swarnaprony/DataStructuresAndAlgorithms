class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_value(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if temp.value < new_node.value:
                    if temp.right == None:
                        temp.right = new_node
                        return True
                    temp = temp.right
                if temp.value > new_node.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True
                    temp = temp.left

    
    def contains(self, value):
        msg = "value found"
        if self.root == None:
            return False
        else:
            temp = self.root
            while temp!= None:
                if value == temp.value:
                    return msg
                if temp.value < value:
                    if temp.right == None:
                        msg = "value not found"
                        return msg
                    temp = temp.right
                if temp.value > value:
                    if temp.left == None:
                        msg = "value not found"
                        return msg
                    temp = temp.left

    def minimum_value(self):
        temp = self.root
        while temp.left != None:
            temp = temp.left
        return temp.value

    def minimum_value_node(self, current_node):
        while current_node.left != None:
            current_node = current_node.left
        return current_node.value

    def breath_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def depth_first_search_preorder(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def depth_first_search_postorder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def depth_first_search_inorder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


my_binary_search_tree = BinarySearchTree()
my_binary_search_tree.insert_value(2)
my_binary_search_tree.insert_value(2)
my_binary_search_tree.insert_value(3)
my_binary_search_tree.insert_value(1)
my_binary_search_tree.insert_value(7)
my_binary_search_tree.insert_value(-2)

print(my_binary_search_tree.root.right.value)
print(my_binary_search_tree.contains(4))
print(my_binary_search_tree.minimum_value())
print(my_binary_search_tree.minimum_value_node(my_binary_search_tree.root.right))
print(my_binary_search_tree.breath_first_search())
print(my_binary_search_tree.depth_first_search_preorder())
print(my_binary_search_tree.depth_first_search_postorder())
print(my_binary_search_tree.depth_first_search_inorder())
