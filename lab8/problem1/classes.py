# BST Classes for Python Implementation

# Python 2.7

class LinkedList: 
  def printBackward(self): 
    print "[", 
    if self.head != None: 
      self.head.printBackward() 
    print "]", 
	
  def addFirst(self, cargo): 
    node = Node(cargo) 
    node.next = self.head 
    self.head = node 
    self.length = self.length + 1

class Node: 
  def printBackward(self): 
    if self.next != None: 
      tail = self.next 
      tail.printBackward() 
    print self.cargo, 
	
  def printList(node): 
    while node: 
      print node, 
      node = node.next 
    print
  
class Stack : 
  def __init__(self) : 
    self.items = [] 

  def push(self, item) : 
    self.items.append(item) 

  def pop(self) : 
    return self.items.pop() 

  def isEmpty(self) : 
    return (self.items == []) 

def evalPostfix(expr): 
  import re 
  tokenList = re.split("([^0-9])", expr) 
  stack = Stack() 
  for token in tokenList: 
    if  token == '' or token == ' ': 
      continue 
    if  token == '+': 
      sum = stack.pop() + stack.pop() 
      stack.push(sum) 
    elif token == '*': 
      product = stack.pop() * stack.pop() 
      stack.push(product) 
    else: 
      stack.push(int(token)) 
  return stack.pop() 
  
class Queue: 
  def __init__(self): 
    self.length = 0 
    self.head   = None 
    self.last   = None 

  def isEmpty(self): 
    return (self.length == 0) 

  def insert(self, cargo): 
    node = Node(cargo) 
    node.next = None 
    if self.length == 0: 
      # if list is empty, the new node is head and last 
      self.head = self.last = node 
    else: 
      # find the last node 
      last = self.last 
      # append the new node 
      last.next = node 
      self.last = node 
    self.length = self.length + 1  

  def remove(self): 
    cargo = self.head.cargo 
    self.head = self.head.next 
    self.length = self.length - 1 
    return cargo 
	
class PriorityQueue: 
  def __init__(self): 
    self.items = [] 

  def isEmpty(self): 
    return self.items == [] 

  def insert(self, item): 
    self.items.append(item) 
  
  def remove(self): 
    maxi = 0 
    for i in range(1,len(self.items)): 
      if self.items[i] > self.items[maxi]: 
        maxi = i 
    item = self.items[maxi] 
    self.items[maxi:maxi+1] = [] 
    return item 
	
class Tree: 
  def __init__(self, cargo, left=None, right=None): 
    self.cargo = cargo 
    self.left  = left 
    self.right = right 

  def __str__(self): 
    return str(self.cargo) 
	
  def total(tree): 
    if tree == None: return 0 
    return total(tree.left) + total(tree.right) + tree.cargo 
	
  def printTree(tree): 
    if tree == None: return 
    print tree.cargo, 
    printTree(tree.left) 
    printTree(tree.right) 

  def printTreePostorder(tree): 
    if tree == None: return 
    printTreePostorder(tree.left) 
    printTreePostorder(tree.right) 
    print tree.cargo
	
def printTreeInorder(tree): 
  if tree == None: return 
  printTreeInorder(tree.left) 
  print tree.cargo, 
  printTreeInorder(tree.right) 
  
  def printTreeIndented(tree, level=0): 
    if tree == None: return 
    printTreeIndented(tree.right, level+1) 
    print '  '*level + str(tree.cargo) 
    printTreeIndented(tree.left, level+1) 