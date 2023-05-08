class TreeNode:
    def __init__(self, data=0, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left
    
    
def preorder_traversal(rootNode: TreeNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preorder_traversal(rootNode.left)
    preorder_traversal(rootNode.right)


def inorder_traversal(rootNode: TreeNode):
    if rootNode is None:
        return
    inorder_traversal(rootNode.left)
    print(rootNode.data)
    inorder_traversal(rootNode.right)
    
def postorder_traversal(rootNode: TreeNode):
    if rootNode is None:
        return
    postorder_traversal(rootNode.left)
    postorder_traversal(rootNode.right)
    print(rootNode.data)
    
    

# 测试代码
#     1
#    / \
#   2   3
#  / \
# 4   5
rootNode = TreeNode(1)
rootNode.left = TreeNode(2)
rootNode.right = TreeNode(3)
rootNode.left.left = TreeNode(4)
rootNode.left.right = TreeNode(5)

print("前序遍历 START----------")
preorder_traversal(rootNode)
print("前序遍历 END------------")


print("中序遍历 START----------")
inorder_traversal(rootNode)
print("中序遍历 END------------")
    
print("后序遍历 START----------")
postorder_traversal(rootNode)
print("后序遍历 END------------")
    