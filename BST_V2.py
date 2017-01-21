#coding by Pasindu Weerasinghe
class Tnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,value):
        if(value<self.data):
            if self.left:
                self.left.insert(value)
            else:
                self.left=Tnode(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right=Tnode(value)

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
        
    def lookup(self,value):
        if self.data==value:
            return True
        else:
            if(value<self.data):
                if self.left:
                    return self.left.lookup(value)
                else:
                    return False
            else:
                if self.right:
                    return self.right.lookup(value)
                else:
                    return False

    def hasnochild(self):
        if self.left ==None and self.right==None:
            return True
        else:
            return False

    def hastwochild(self):
        if self.left and self.right:
            return True
        else:
            return False

    def hasonechild(self):
        if self.left  and self.right:
            return False
        elif self.left!=None or self.right!=None:
            return True
        else:
            return False

               
            
            
            
        
            
class Tree:
    def __init__(self):
        self.root=None

    def addNode(self,value):
        if self.root:
            self.root.insert(value)
        else:
            self.root=Tnode(value)

    def preorder(self):
        if self.root:
            self.root.preorder()
    def inorder(self):
        if self.root:
            self.root.inorder()
    def postorder(self):
        if self.root:
            self.root.postorder()
    def lookup(self,value):
        if self.root:
            return self.root.lookup(value)

    def remove(self,value):
        parent=None
        cur=self.root
        while(True):
            if value<cur.data:
                if cur.left.data==value:
                    parent=cur
                    cur=cur.left
                    break
                else:
                    cur=cur.left
            else:
                if cur.right.data==value:
                    parent=cur
                    cur=cur.right
                    break
                else:
                    cur=cur.right

        if cur.hasnochild()==True:
            if parent.left.data==cur.data:
                parent.left=None
            elif parent.right.data==cur.data:
                parent.right=None

        elif cur.hasonechild()==True:
            if parent.left.data==cur.data:
                if cur.left!=None:
                    parent.left=cur.left
                else:
                    parent.left=cur.right
            
            elif parent.right.data==cur.data:
                if cur.left!=None:
                    parent.right=cur.left
                else:
                    parent.right=cur.right
        #there is no implent for the if node has two child.it is difficult 
        

t=Tree()
t.addNode(5)
t.addNode(2)
t.addNode(18)
t.addNode(-4)
t.addNode(3)
t.addNode(21)
t.addNode(19)
t.addNode(25)

t.remove(2)
t.preorder()
#t.inorder()
#t.postorder()
#print(t.lookup(6))
