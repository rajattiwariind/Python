class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def count_nodes(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Main
ll = SinglyLinkedList()
ll.insert_at_head("Apple")
ll.insert_at_head("Mango")
ll.insert_at_head("PineApple")
ll.insert_at_head("Pear")
ll.insert_at_head("Cherry")
print(ll.search("Mango")) 
ll.print_list() 
print(ll.count_nodes()) 
ll.delete("Pear")
ll.print_list() 
