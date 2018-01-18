class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    temp = root
    if (temp is not None):
        inorder(temp.left)
        print (temp.data)
        inorder(temp.right)

def insert(node, new_data):

    if (node is None):
        newNode = Node(new_data)
        return newNode

    if (new_data < node.data):
        node.left = insert(node.left,new_data)

    elif (new_data > node.data):
        node.right = insert(node.right,new_data)

    return node


def minvalue(node):
    temp = node

    while (temp.left is not None):
        temp = temp.left

    return temp


def delete(root, key):
 
    if root is None:
        return root 
 
   
    if key < root.data:
        root.left = delete(root.left, key)
 
    
    elif(key > root.data):
        root.right = delete(root.right, key)
 
   
    else:
         
        
        if root.left is None :
            temp = root.right 
            root = None
            return temp 
             
        elif root.right is None :
            temp = root.left 
            root = None
            return temp
 
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minvalue(root.right)
 
        # Copy the inorder successor's content to this node
        root.data = temp.data
 
        # Delete the inorder successor
        root.right = delete(root.right , temp.data)
 
 
    return root 


root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
     
print ("Inorder traversal of the given tree")
inorder(root)
     
print ("\nDelete 20")
root = delete(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)
     
print ("\nDelete 30")
root = delete(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)
     
print ("\nDelete 50")
root = delete(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)
