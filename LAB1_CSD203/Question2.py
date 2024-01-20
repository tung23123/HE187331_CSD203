class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAfter(self, p, x):
        new_node = Node(x)
        current = self.head
        while current and current.data != p:
            current = current.next
        if not current:
            print(f"Node with value {p} not found.")
            return
        new_node.next = current.next
        current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        print('\n')

    def deleteFromHead(self):
        if not self.head:
            print("List is empty.")
            return None
        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data

    def deleteFromTail(self):
        if not self.head:
            print("List is empty.")
            return None
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_data = current.next.data
        current.next = None
        return deleted_data

    def deleteAfter(self, p):
        current = self.head
        while current and current.data != p:
            current = current.next
        if not current or not current.next:
            print(f"Node with value {p} not found or no node after it.")
            return None
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def delete(self, x):
        if not self.head:
            print("List is empty.")
            return None
        if self.head.data == x:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data
        current = self.head
        while current.next and current.next.data != x:
            current = current.next
        if not current.next:
            print(f"Node with value {x} not found.")
            return None
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def search(self, x):
        current = self.head
        while current and current.data != x:
            current = current.next
        if current:
            print('Found mode with values ',x)
        else:
            print('Node not found')

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    print(''''Linked list after add 'A' to Head:''')
    linked_list.addToHead("A")
    linked_list.traverse()

    print(''''Linked list after add 'B' and 'C' to Tail:''')
    linked_list.addToTail("B")
    linked_list.addToTail("C")
    linked_list.traverse()

    linked_list.addAfter("B", "D")
    print(''''Linked list after add 'D' after 'C':''')
    linked_list.traverse()

    linked_list.deleteFromHead()
    print('Linked list after delete from Head: ')
    linked_list.traverse()

    linked_list.deleteFromTail()
    print('Linked list after delete from Tail: ')
    linked_list.traverse()

    linked_list.deleteAfter("B")
    print(''''Linked list after delete after 'B': ''')
    linked_list.traverse()

    linked_list.delete("D")
    print('''Linked list after delete 'D': ''')
    linked_list.traverse()

    linked_list.search("B")

    print("Number of nodes in the list:", linked_list.count())
