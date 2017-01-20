#coding by Pasindu Weerasinghe
class Stack:
    def __init__(self):
        self.list=[]

    def push(self,item):
        self.list.append(item)

    def pop(self):
        self.list.pop()

    def peek(self):
        return self.list[len(self.list)-1]

    def isEmpty(self):
        return len(self.list)==0

    def printS(self):
        return self.list[:]

    
#test

S=Stack()
S.push(10)
S.push(20)
S.push(30)
S.pop()
S.push(450)
print(S.peek())
print(S.printS())

