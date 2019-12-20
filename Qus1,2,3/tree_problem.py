
class Node: 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None

def addGreaterUtil(root, sum_ptr): 
	if root == None: 
		return
	addGreaterUtil(root.right, sum_ptr) 
	sum_ptr[0] = sum_ptr[0] + root.key 
	root.key = sum_ptr[0] 
	addGreaterUtil(root.left, sum_ptr) 
def addGreater(root): 
	Sum = [0] 
	addGreaterUtil(root, Sum) 
def printInorder(node): 
	if node == None: 
		return
	printInorder(node.left) 
	print(node.key, end = " ") 
	printInorder(node.right) 

root = Node(5) 
root.left = Node(3) 
root.left.left=Node(2)
root.left.right=Node(4)
root.right = Node(8)
root.right.left=Node(6)
root.right.right=Node(10)
print("Inorder of the given tree") 
printInorder(root) 
addGreater(root) 
print("Inorder of the modified tree") 
printInorder(root) 

