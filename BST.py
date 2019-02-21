from Node import Node

class BST(object):
    def __init__(self):
        self.__root = None

    def getRoot(self):
        # Private Method, can only be used inside of BST.
        return self.__root

    def __findNode(self, data):
        # Private Method, can only be used inside of BST.
        # Search tree for a node whose data field is equal to data.
        # Return the Node object
        x = self.__root

        while x is not None and data != x.getData():
            if data < x.getData():
                x = x.getLeftChild()
            else:
                x = x.getRightChild()
        return x

    def contains(self, top, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        if top is None:
            return false
        if top.getData() == data:
            return true
        if top.getData() > data:
            return self.contains(top.getLeftChild(), data)
        return self.contains(top.getRightChild, data)

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error
        y = None
        x = self.__root
        z = Node(data)

        while x != None:
            y = x
            if z.getData() < x.getData():
                x = x.getLeftChild()
            else:
                x = x.getRightChild()
        z.setParent(y)
        if y == None:
            self.__root = z # case for tree being empty
        elif z.getData() < y.getData():
            y.setLeftChild(z)
        else:
            y.setRightChild(z)

        #pass
    
    def delete(self,top,data):
        #base case
        if top is None:
            return top
        #if key to be deleted is smaller than root's key then left subtree
        if data < top.getData():
            top.setLeftChild(delete(top.getLeftChild, data))

        #if key is greater than root is in right subtree
        elif data > top.getData():
            top.setRightChild(delete(top.getRightChild(), data))

        #if key is root's data, then root needs to be deleted
        else:
            #node with one or no child
            if top.getLeftChild() is None:
                temp = top.getRightChild()
                top = None
                return temp

            elif top.getRightChild is None:
                temp = root.getLeftChild()
                top = None
                return temp

            #node with two children, get successor
            temp = self.treeMin(top.getRightChild())

            #copy successor to this node
            top.setData(temp.getData())
        return top
    def deleteBook(self, data):
        # Find the node to delete.
        # If the value does not exist in the tree, then don't change the tree.
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove 
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node 
        # in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() 
	#to find the successor when there are two children

        z = self.__findNode(data)

        if z.getLeftChild() is None: #case for z having no left child
            transplant(z,z.getRightChild)
        elif z.getRightChild() is None: #case for z having left child but no right child
            transplant(z,z.getLeftChild())
        else:
            y = self.treeMin(z.getRightChild())
            if y.getParent() is not z:
                self.transplant(y,y.getRightChild())
                y.setRightChild(z.getRightChild())
                y.getRightChild().setParent(y)
            self.transplant(z,y)
            y.setLeftChild(z.getLeftChild())
            y.getLeftChild().setParent(y)

        return None

    def treeMin(self, x):
        while x.getLeftChild() is not None:
            x = x.getLeftChild()
        return x

    def transplant(self, u, v):
        if u.getParent() is None: #case where u is the root of the tree
            self.__root = v
        elif u is u.getParent().getLeftChild(): # case where u is the left child of its parent
            u.getParent().setLeftChild(v)
        else:
            u.getParent().setRightChild(v) # case where u is the right child of its parent
        if v is not None:
            v.setParent(u.getParent())

    def __findSuccessor(self, x):
        if x.getRightChild() is not None:
            return treeMin(x.getRightChild())
        y = x.getParent()
        while y != None and x == y.getRightChild():
            x = y
            y = y.getParent()
        return y

    def traverse(self, order, top):
        # traverse the tree by printing out the node data for all node 
        #in a specified order

        if top is not None:
            if order == "preorder":
                if top != None:
                    print top.getData(),
                    self.traverse(order, top.getLeftChild())
                    self.traverse(order, top.getRightChild())
            
            elif order == "inorder":
                if top != None:
                    self.traverse(order, top.getLeftChild())
                    print top.getData(),
                    self.traverse(order, top.getRightChild())

            elif order == "postorder":
                if top != None:
                    self.traverse(order, top.getLeftChild())
                    self.traverse(order, top.getRightChild())
                    print top.getData(),
            
            else:
                print("Error, order {} undefined".format(order))
