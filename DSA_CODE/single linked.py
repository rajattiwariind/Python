#menu driven application for single linked list
class Node:
       def __init__(self,data):
              self.data=data
              self.next=None
class slinkedlist:
       def __init__(self):
              self.head=None
       def is_empty(self):
              return self.head is None
       def insert_at_head(self,data):
              new_node=Node(data)
              new_node.next=self.head
              self.head=new_node
       def insert_at_tail(self,data):
              new_node=Node(data)
              if self.is_empty():
                     self.head=new_node
              else:
                     current=self.head
                     while current.next:
                            current=current.next
                     current.next=new_node
       def delete(self,data):
              if self.is_empty():
                     return
              if self.head.data==data:
                     self.head=self.head.next
                     return
              current=self.head
              while current.next:
                     if current.next.data==data:
                            current.next=current.next.next
                            return
                     current=current.next
       def search(self,data):
              current=self.head
              while current:
                     if current.data==data:
                            return True
                     current=current.next
       def print_list(self):
              current=self.head
              while current:
                     print(current.data,end="  ")
                     current=current.next
              print()
#main
def display():
       print("\nMenu")
       print("1.Insert at head.")
       print("2.Insert at tail.")
       print("3.Delete element.")
       print("4.Search an element.")
       print("5. Print list.")
       print("6. Exit.")
def menu():
       s=slinkedlist()
       while True:
              display()
              a=int(input("Select from menu:"))
              if a==1:
                     b=input("Enter element to be inserted at head:")
                     s.insert_at_head(b)
              elif a==2:
                     b=input("Enter element to be inserted at tail:")
                     s.insert_at_tail(b)
              elif a==3:
                     b=input("Enter element to be deleted:")
                     s.delete(b)
              elif a==4:
                     b=input("Enter element to be searched:")
                     s.search(b)
              elif a==5:
                     print("Printed list is:")
                     s.print_list()
              elif a==6:
                     print("Exiting List.")
                     break
              else:
                     print("Inavlid choice. we don't have this option.")
menu()
