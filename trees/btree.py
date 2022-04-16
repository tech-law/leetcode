class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode('root')
node1 = TreeNode('child1')
node2 = TreeNode('child2')
node3 = TreeNode('child11')
node4 = TreeNode('child12')

node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4

tree = node0

print(tree.left.key)
print(tree.right.key)
print(tree.key)

def height(tree):
    if tree:
        return 1 + max(height(tree.left), height(tree.right))
    else: return 0

def tree_from_tuple(data):

    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = tree_from_tuple(data[0])
        node.right = tree_from_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

t = (((3,4,5),2,(6,7,8)), 1, ((10,11,12),9,(13,14,15)))

tree = tree_from_tuple(t)
print(height(tree))

def tree_to_tuple(tree):
    if tree:
        return (tree_to_tuple(tree.left), tree.key, tree_to_tuple(tree.right))

def tree_to_tuple_trim(tree):
    if tree:
        if tree.left and tree.right:
            return (tree_to_tuple_trim(tree.left), tree.key, tree_to_tuple_trim(tree.right))
        elif tree.left:
            return (tree_to_tuple_trim(tree.left), tree.key, None)
        elif tree.right:
            return (None, tree.key, tree_to_tuple_trim(tree.right))
        else: 
            return tree.key 
            
        
print(t)
print(tree_to_tuple(tree))
print(tree_to_tuple_trim(tree))


print(height(tree))