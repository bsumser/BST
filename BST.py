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
        pass

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        pass

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
    
    def delete(self, data):
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

        return None

    def __findSuccessor(self, aNode):
        pass

    def traverse(self, order, top):
        # traverse the tree by printing out the node data for all node 
        #in a specified order

        if top is not None:
            if order == "preorder":
                # your code here, remove pass
                pass
                
            
            elif order == "inorder":
                # your code here, remove pass
                pass


            elif order == "postorder":
                # your code here, remove pass
                pass
            
            else:
                print("Error, order {} undefined".format(order))

