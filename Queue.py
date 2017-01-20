#coding by Pasindu Weerasinghe
class Queue:
    def __init__(self):
        self.list=[]

    def enqueue(self,item):
        self.list.append(item)

    def dequeue(self):
        self.list.remove(self.list[0])

    def peek(self):
        return self.list[0]

    def isEmpty(self):
        return len(self.list)==0

    def printQ(self):
        return self.list[:]



#test

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
print(q.peek())
