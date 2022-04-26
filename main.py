from encodings import search_function
from typing import List


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                self.left = self.__insert_node(node=self.left, value=value)
            
            elif value > self.value:
                self.right = self.__insert_node(node=self.right, value=value)


    def __insert_node(self, node, value):
        if node is None:
            node = Node(value) 
        else:
            node.insert(value)

        return node
    
    def in_order(self, elements: List):
        
        if self.left:
            self.left.in_order(elements)
        
        elements.append(self.value)

        if self.right:
            self.right.in_order(elements)

    def pre_order(self, elements: List):

        elements.append(self.value)

        if self.left:
            self.left.pre_order(elements)
        
        if self.right:
            self.right.pre_order(elements)

    def post_order(self, elements: List):
        
        if self.left:
            self.left.post_order(elements)
        
        if self.right:
            self.right.post_order(elements)
        
        elements.append(self.value)


    
    def search(self, value):

        if value == self.value:
            return self
        
        elif value < self.value:

            if self.left:
                return self.left.search(value)
            else:
                return None
            
        elif value > self.value:

            if self.right:
                return self.right.search(value)
            else:
                return None
    
    def __str__(self) -> str:
            show_info = ''
            if self.left:
                show_info += f'({self.left.value}) <-- '
            
            show_info += f'[{self.value}]'
            
            if self.right:
                show_info += f' --> ({self.right.value})'
            
            return show_info


class BinaryTree:
    def __init__(self, value) -> None:
        self.root: Node = Node(value=value)

    def insert_value(self, value):
        self.root.insert(value)
    
    def search(self, value):

        result = self.root.search(value=value)

        if not result:
            print(f'value {value} not found in tree')
        else:
            print(f'value found in node: {result}')



    def print_traversal(self, traversal_type='in'):
        elements = []

        if traversal_type == 'post':
            self.root.post_order(elements)
        elif traversal_type == 'pre':
            self.root.pre_order(elements)
        else:
            self.root.in_order(elements)

        print(elements)

    def print_tree(self, node: Node, is_root=False):

        if node and (node.left or node.right or is_root):

            print(node)
            self.print_tree(node.left)
            self.print_tree(node.right)
            




tree = BinaryTree(value=10)

array = [6, 7, 2, 15, 12, 20]

for i in range(len(array)):
    tree.insert_value(value=array[i])

print('\n tree structure: ')
tree.print_tree(node=tree.root, is_root=True)

print('\nin order trasversal:')
tree.print_traversal(traversal_type='in')

print('\npre order trasversal:')
tree.print_traversal(traversal_type='pre')

print('\npost order trasversal:')
tree.print_traversal(traversal_type='post')

search_value = 15
print(f'\nsearch value: {search_value}')
tree.search(value=search_value)
