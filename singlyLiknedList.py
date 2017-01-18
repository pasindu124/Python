class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def addNode(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            cur=self.head
            while(cur.next!=None):
                cur=cur.next
            cur.next=newNode

    def removeNode(self,data):
        cur=self.head
        if cur.data==data:
            if cur.next==None:
                self.head=None
            else:
                self.head=cur.next
        else:
            while(cur.next.data!=data):
                cur=cur.next
            if cur.next.next==None:
                cur.next=None
            else:
                cur.next=cur.next.next

    def findNode(self,data):
        cur=self.head
        while(cur):
            if cur.data==data:
                return True
            else:
                cur=cur.next
        return False
            

    def displayList(self):
        cur=self.head
        while(cur.next!=None):
            print(cur.data ,end=",")
            cur=cur.next
        print(cur.data)

l=Linkedlist()
l.addNode(10)
l.addNode(20)
l.addNode(30)
l.removeNode(30)
l.displayList()
l.addNode(45)

            
