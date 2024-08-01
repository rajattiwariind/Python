class circular_queue:
       def __init__(self,k):
              self.k=k
              self.queue=[None]*k
              self.head=-1
              self.tail=-1
       def enqueue(self,value):
              if self.is_full():
                     print("Queue is full")
              elif self.is_empty():
                     self.head=0
                     self.tail=0
                     self.queue[self.tail]=value
              else:
                     self.tail=(self.tail+1)%self.k
                     self.queue[self.tail]=value
       def dequeue(self):
              if self.is_empty():
                     print("Queue is Empty")
                     return None
              value=self.queue[self.head]
              if self.head==self.tail:
                     self.head=-1
                     self.tail=-1
              else:
                     value=self.queue[self.head]
                     self.head=(self.head+1)%self.k
              return value 
       def is_full(self):
              return (self.tail+1)%self.k==self.head
       def display(self):
              if self.is_empty():
                     print("Queue is Empty")
              elif self.tail>=self.head:
                     for i in range(self.head,self.k):
                            print(self.queue[i],end=" ")
                     print()
              else:
                     for i in range(self.head,self.k):
                            print(self.queue[i],end=" ")
                     for i in range(0,self.tail+1):
                            print(self.queue[i],end=" ")
                     print()
       def is_empty(self):
              return self.head==-1
#main
queu=circular_queue(5)
queu.enqueue(1)
queu.enqueue(2)
queu.enqueue(3)
queu.enqueue(4)
queu.enqueue(5)
queu.display()
queu.dequeue()
print("check for queue full",queu.is_full())
print("check for queue empty",queu.is_empty())
queu.display()

