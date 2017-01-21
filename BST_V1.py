#coding by Pasindu Weerasinghe
class Tnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def addNode(self,data):
        newNode=Tnode(data)
        if self.root==None:
            self.root=newNode
        else:
            cur=self.root
            while(True):
                if(data<cur.data):
                    if cur.left==None:
                        cur.left=newNode
                        break
                    else:
                        cur=cur.left
                else:
                    if cur.right==None:
                        cur.right=newNode
                        break
                    else:
                        cur=cur.right

    def lookup(self,data):
        if self.root.data==data:
            return True
        else:
            cur=self.root
            while(True):
                if(data<cur.data):
                    if cur.left:
                        if cur.left.data==data:
                            return True
                        else:
                            cur=cur.left
                    else:
                        return False
                else:
                    if cur.right:
                        if cur.right.data==data:
                            return True
                        else:
                            cur=cur.right
                    else:
                        return False
                
    def preorder(self,node):
        print(node.data)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def inorder(self,node):
        if node.left:
            self.inorder(node.left)
        print(node.data)
        if node.right:
            self.inorder(node.right)

    def postorder(self,node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.data)
        
        
    
t=Tree()
t.addNode(7)
t.addNode(1)
t.addNode(9)
t.addNode(0)
t.addNode(3)
t.addNode(8)
t.addNode(10)
t.addNode(2)
t.addNode(5)
t.addNode(4)
t.addNode(6)
#t.preorder(t.root)
#t.inorder(t.root)
#t.postorder(t.root)
print(t.lookup(15))
