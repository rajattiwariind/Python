class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end="\n")
                current = current.next
            print()

    def print_reverse(self):
        if self.tail is None:
            print("List is empty")
        else:
            current = self.tail
            while current is not None:
                print(current.data, end="\n")
                current = current.prev
            print()

    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def insert_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_middle(self, data):
        # This method needs to be implemented based on specific requirements.
        pass

    def peek_front(self):
        if self.head is None:
            return "List is empty"
        else:
            return self.head.data

    def peek_tail(self):
        if self.tail is None:
            return "List is empty"
        else:
            return self.tail.data

    def delete_head(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp = self.head
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            temp.next = None
            return temp.data

    def delete_tail(self):
        if self.tail is None:
            print("List is empty")
            return
        else:
            temp = self.tail
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            temp.prev = None
            return temp.data

    def display(self):
        print("\nMenu")
        print("1. Insert at head.")
        print("2. Insert at tail.")
        print("3. Delete element from head.")
        print("4. Delete element from tail.")
        print("5. Peek front element from list.")
        print("6. Peek tail element from list.")
        print("7. Reverse the list.")
        print("8. Print list.")
        print("9. Exit.")

# Main loop
d = DoublyLinkedList()
while True:
    d.display()
    a = int(input("Select from menu: "))
    if a == 1:
        b = input("Enter element to be inserted at head: ")
        d.insert_at_begin(b)
    elif a == 2:
        b = input("Enter element to be inserted at tail: ")
        d.insert_tail(b)
    elif a == 3:
        d.delete_at_begin()
    elif a == 4:
        d.delete_tail()
    elif a == 5:
        print("Front element of list: ", d.peek_front())
    elif a == 6:
        print("Back element of list: ", d.peek_tail())
    elif a == 7:
        print("Reversed list:")
        d.print_reverse()
    elif a == 8:
        print("Printed list is:")
        d.print_list()
    elif a == 9:
        print("Exiting List.")
        break
    else:
        print("Invalid choice. We don't have this option.")
