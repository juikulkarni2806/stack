class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def print(self):
        temp=self.front

        while temp:
            print(temp.data, end="->")
            temp=temp.next

lq=Queue()
lq.enqueue(Node(15))
lq.enqueue(Node(24))
lq.enqueue(Node(33))
lq.enqueue(Node(42))
lq.enqueue(Node(51))
lq.enqueue(Node(60))
lq.print()


