def traverse_binary_tree(node, callback):
    if node is None:
        return
    traverse_binary_tree(node.leftChild, callback)
    callback(node.value)
    traverse_binary_tree(node.rightChild, callback)

def search_recursively(key, node):
	if node is None or node.key == key:
		return node
	elif key < node.key:
		return search_recursively(key, node.left)
	else:  # key > node.key
		return search_recursively(key, node.right)
	return None

def search_iteratively(key, node): 
	current_node = node
	while current_node is not None:
		if key == current_node.key:
			return current_node
		elif key < current_node.key:
			current_node = current_node.left
		else:  # key > current_node.key:
			current_node = current_node.right
	return None

def find_min(self):   # Gets minimum node in a subtree
    current_node = self
    while current_node.left_child:
        current_node = current_node.left_child
    return current_node

def replace_node_in_parent(self, new_value=None):
    if self.parent:
        if self == self.parent.left_child:
            self.parent.left_child = new_value
        else:
            self.parent.right_child = new_value
    if new_value:
        new_value.parent = self.parent

def binary_tree_delete(self, key):
    if key < self.key:
        self.left_child.binary_tree_delete(key)
    elif key > self.key:
        self.right_child.binary_tree_delete(key)
    else: # delete the key here
        if self.left_child and self.right_child: # if both children are present
            successor = self.right_child.find_min()
            self.key = successor.key
            successor.binary_tree_delete(successor.key)
        elif self.left_child:   # if the node has only a *left* child
            self.replace_node_in_parent(self.left_child)
        elif self.right_child:  # if the node has only a *right* child
            self.replace_node_in_parent(self.right_child)
        else: # this node has no children
            self.replace_node_in_parent(None)