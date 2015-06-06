class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data,
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print root.data,
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
	
def post_order_print(root):
	if not root:
		return        
	pre_order_print(root.l_child)
	pre_order_print(root.r_child)
	print root.data,

def trace_depth(root, depth):
	global global_depth
	if not root:
		return
	print "data field ",
	print root.data,
	print " depth ",
	print depth
	global_depth = depth
	depth = depth + 1
	trace_depth(root.l_child, depth)
	trace_depth(root.r_child, depth)
	depth = depth - 1
	

def compute_depth(root):
	print global_depth

	
	
print "Enter integers for Binary Search Tree. End with 0."
inputnumber = 7
iteration = 0
roots = 0
global_depth=0

inlist = []
while inputnumber > 0:
	inputnumber=input()
	if inputnumber > 0:
		inlist.append(inputnumber)
	else:
		break
	iteration += 1

print "you entered " + str(inlist)

root = Node(inlist[0])

for i in range(1, len(inlist)):
	binary_insert(root, Node(inlist[i]))
	
	
print "Pre Order:"
pre_order_print(root)
print
print
print "In Order:"
in_order_print(root)
print
print
print "Post Order:"
post_order_print(root)
print
print
print "Trace Depth:"
trace_depth(root, 0)

print "BST Depth:"
compute_depth(root)
print
print
print "Number of Nodes:"
print iteration

