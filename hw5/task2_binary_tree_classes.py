class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        elif value == node.value:
            raise ValueError("Значение уже присутствует в дереве.")
        
    def find(self, value):
        current_node = self.root
        while current_node != None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
        return False
        
    def delete(self, value):
        current_node = self.root
        parent = None
        while current_node != None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                if current_node.left == None:
                    if parent == None:  # Если это корень
                        self.root = current_node.right
                    elif parent.left == current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                elif current_node.right == None:
                    if parent == None:
                        self.root = current_node.left
                    elif parent.left == current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                else: # Узел с двумя потомками
                    min_right_node = self._find_min(current_node.right)
                    min_value = min_right_node.value
                    self.delete(min_value)
                    current_node.value = min_value
                return True
        return False

    def _find_min(self, node):
        while node.left != None:
            node = node.left
        return node.left
    
    def show(self):
        self._iteration(self.root)
        return
    
    def _iteration(self, node):
        if node != None:
            self._iteration(node.left)
            print(node.value, end="|")
            self._iteration(node.right)
        return
