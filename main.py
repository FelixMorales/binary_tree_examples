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


    def find_min(self):

        min_value = self.value
        if self.left:
            min_value = self.left.find_min()
        
        return min_value

    def find_max(self):

        max_value = self.value
        if self.right:
            max_value = self.right.find_max()

        return max_value

    def delete(self, value):
        
        if value < self.value:
            if self.left:
                new_left = self.left.delete(value)
                self.left = new_left
        
        elif value > self.value:
            if self.right:
                new_right = self.right.delete(value)
                self.right = new_right

        else:
            if self.right is None and self.left is None:
                return None
            
            if self.right is None:
                return self.left
            
            if self.left is None:
                return self.right
            
            max_value = self.left.find_max()

            self.value = max_value
            self.left = self.left.delete(max_value)
        
        return self
    
    def update(self, current_value, new_value):

        self.delete(current_value)

        self.insert(new_value)

    def print_tree(self, is_root=False):
        show_info = ''

        if is_root or self.right or self.left:
            show_info += f'{str(self)} \n'

        if self.left:
            show_info += self.left.print_tree()
        
        if self.right:
            show_info += self.right.print_tree()
        
        return show_info
            
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
    
    def get_max(self):
        return self.root.find_max()
    
    def get_min(self):
        return self.root.find_min()

    
    def delete(self, value):
        return self.root.delete(value)
    
    def update(self, current_value, new_value):
        return self.root.update(current_value=current_value, new_value=new_value)

    def print_traversal(self, traversal_type='in'):
        elements = []

        if traversal_type == 'post':
            self.root.post_order(elements)
        elif traversal_type == 'pre':
            self.root.pre_order(elements)
        else:
            self.root.in_order(elements)

        print(elements)

    def __str__(self):
        return self.root.print_tree(is_root=True)

array = [10, 6, 7, 2, 15, 12, 20, 14, 13]
tree = BinaryTree(value=array[0])

for i in range(1, len(array)):
    tree.insert_value(value=array[i])

print('\narray: ')
print(array)

print('\ntree structure: ')
print(tree)

print('\nin order trasversal:')
tree.print_traversal(traversal_type='in')

print('\npre order trasversal:')
tree.print_traversal(traversal_type='pre')

print('\npost order trasversal:')
tree.print_traversal(traversal_type='post')

search_value = 15
print(f'\nsearch value: {search_value}')
tree.search(value=search_value)

print(f'\nmin value is: {tree.get_min()}')

print(f'\nmax value is: {tree.get_max()}')

delete_value = 10
print(f'\ndelete value: {delete_value}')
tree.delete(delete_value)

print('\ntree after delete: ')
print(tree)

update_value = (15, 25)
print(f'\nupdate value: {update_value[0]} to {update_value[1]}')
tree.update(current_value=update_value[0], new_value=update_value[1])

print('\ntree after update: ')
print(tree)