class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class CQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

        self.rear.next=self.front  #added for circular
    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear==None
                print("Now Queue is Empty")
            self.rear.next=self.front

            temp=None
        else:
            print("Queue is Empty")

    def print(self):
        temp=self.front

        while True:
            print(temp.data, end=" ")
            temp=temp.next
            if temp==self.front:
                break
        print()

lq=CQueue()
lq.enqueue(Node(15))
lq.enqueue(Node(24))
lq.enqueue(Node(33))
lq.enqueue(Node(42))
lq.enqueue(Node(51))
lq.enqueue(Node(60))
lq.print()
lq.dequeue()
lq.dequeue()
lq.dequeue()
lq.print()
lq.enqueue(Node(69))
lq.enqueue(Node(87))
lq.print()