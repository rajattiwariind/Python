class Node:
       def __init__(self,data):
              self.data=data
              self.next=None
class circular_linkedlist:
       def __init__(self):
              self.head=None
       def append(self,data):
              new_node=Node(data)
              if not self.head:
                     self.head=new_node
                     new_node.next=self.head
              else:
                     temp=self.head
                     while temp.next != self.head:
                            temp=temp.next
                     temp.next=new_node
                     new_node.next=self.head
       def print_list(self):
              if not self.head:
                     print("Circular list is empty")
                     return
              temp=self.head
              while True:
                     print(temp.data,end=" ")
                     temp=temp.next
                     if temp==self.head:
                            break
              print("\n")
#main
c=circular_linkedlist()
c.append("idli")
c.append("chai")
c.append("poha")
c.print_list()
