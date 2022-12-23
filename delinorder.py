class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
def insert( node, data):
 
    if node is None:
        return newNode(data)
    else:
        
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
         
        return node
    
def printInorder(root):
 
    if root:
 
        printInorder(root.left)
 
        print(root.data, end = ' '),
 
        printInorder(root.right)
    
def deleteNode(root, key):
  
    if root is None:
        return root
     
    if key < root.data:
        root.left = deleteNode(root.left, key)
      
    elif(key > root.data):
        root.right = deleteNode(root.right, key)
      
    else:
  
        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp
          
        temp = minValueNode(root.right)
  
        root.key = temp.key
  
        root.right = deleteNode(root.right, temp.key)
  
    return root
    
def minValue(node):
    current = node
 
    while(current is not None):
        if current.left is None:
            break
        current = current.left
 
    return current
def inOrderSuccessor(n):

    if n.right is not None:
        return minValue(n.right)
 
    p = n.parent
    while( p is not None):
        if n != p.right :
            break
        n = p
        p = p.parent
    return p.data

def delinorder(n):
    succ = inOrderSuccessor(n)
    if succ is not None:
        return deleteNode(root,succ.data)

root= newNode(1)
insert(root,2)
insert(root,3)
insert(root,4)
insert(root,5)
insert(root,6)
insert(root,7)
insert(root,8)

temp = root.right
succ = inOrderSuccessor(temp)
if succ is not None:
    print (f"\nInorder Successor of {temp.data} is {succ.data} ")
else:
    print ("\nInorder Successor doesn't exist")
delinorder(temp)
print('\nAfter deleting successor: ')
printInorder(root)
