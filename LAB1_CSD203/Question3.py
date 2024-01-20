class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addAfter(self, p, x):
        new_node = Node(x)
        current = self.head
        while current and current.data != p:
            current = current.next
        if not current:
            print(f"Node with value {p} not found.")
            return
        new_node.prev = current
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def deleteFromHead(self):
        if not self.head:
            print("List is empty.")
            return None
        deleted_data = self.head.data
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next
        return deleted_data

    def deleteFromTail(self):
        if not self.head:
            print("List is empty.")
            return None
        deleted_data = self.tail.data
        if self.tail.prev:
            self.tail.prev.next = None
        self.tail = self.tail.prev
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
        if current.next:
            current.next.prev = current
        return deleted_data

    def delete(self, x):
        current = self.head
        while current and current.data != x:
            current = current.next
        if not current:
            print(f"Node with value {x} not found.")
            return None
        deleted_data = current.data
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        return deleted_data

    def search(self, x):
        current = self.head
        while current and current.data != x:
            current = current.next
        return current

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def delAtIndex(self, i):
        current = self.head
        for _ in range(i):
            current = current.next
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev

    def sort(self):
        sorted_list = sorted(self.toArray())
        self.head = None
        self.tail = None
        for value in sorted_list:
            self.addToTail(value)

    def delNode(self, p):
        current = self.head
        while current and current != p:
            current = current.next
        if not current:
            print(f"Node {p} not found.")
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev

    def toArray(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

    def mergeOrderedLists(self, other_list):
        merged_list = DoublyLinkedList()
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.data < current2.data:
                merged_list.addToTail(current1.data)
                current1 = current1.next
            else:
                merged_list.addToTail(current2.data)
                current2 = current2.next

        while current1:
            merged_list.addToTail(current1.data)
            current1 = current1.next

        while current2:
            merged_list.addToTail(current2.data)
            current2 = current2.next

        return merged_list

    def addBefore(self, p, x):
        new_node = Node(x)
        current = self.head
        while current and current != p:
            current = current.next
        if not current:
            print(f"Node {p} not found.")
            return
        new_node.prev = current.prev
        new_node.next = current
        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node
        current.prev = new_node

    def attachList(self, other_list):
        if not self.head:
            self.head = other_list.head
            self.tail = other_list.tail
        else:
            self.tail.next = other_list.head
            if other_list.head:
                other_list.head.prev = self.tail
            self.tail = other_list.tail

    def max(self):
        if not self.head:
            return None
        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def min(self):
        if not self.head:
            return None
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def sum(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def avg(self):
        count = self.count()
        if count == 0:
            return None
        return self.sum() / count

    def sorted(self):
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def insert(self, x):
        new_node = Node(x)
        current = self.head
        while current and current.data < x:
            current = current.next

        if current:
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            else:
                self.head = new_node
            current.prev = new_node


# Example usage:
linked_list = DoublyLinkedList()
print('List after add 5 to Head: ')
linked_list.addToHead(5)
linked_list.traverse()
linked_list.addToTail(3)
linked_list.addToTail(7)
print('List after add 3, 7 to Tail: ')
linked_list.traverse()

linked_list.addAfter(3, 6)
print('List after add 6 after 3: ')
linked_list.traverse()

print('Traverse list: ')
linked_list.traverse()

linked_list.deleteFromHead()
print('List after delete from Head: ')
linked_list.traverse()

linked_list.deleteFromTail()
print('List after delete from Tail: ')
linked_list.traverse()

linked_list.deleteAfter(3)
print('List after delete node after 3:')
linked_list.traverse()

linked_list.delNode(6)
print('List after delete 6: ')
linked_list.traverse()

print('Number of element in list is: ',linked_list.count())

linked_list.sort()
print('List after delete sort:')
linked_list.traverse()

print('create and return Array value of all nodes in list:')
print(linked_list.toArray())

print("Merged List:")
list1 = DoublyLinkedList()
list1.addToTail(2)
list1.addToTail(4)
list1.addToTail(6)

list2 = DoublyLinkedList()
list2.addToTail(1)
list2.addToTail(3)
list2.addToTail(5)

merged_list = list1.mergeOrderedLists(list2)
merged_list.traverse()
print('two Original lists: ')
list1.traverse()
list2.traverse()
print('After merge into one ordered list: ')
merged_list.traverse()

linked_list.addBefore(7, 8)
print('List after add 8 before 7:')
linked_list.traverse()

new_list = DoublyLinkedList()
new_list.addToTail(9)
new_list.addToTail(10)
print('two original list: ')
linked_list.traverse()
new_list.traverse()
linked_list.attachList(new_list)
print('after attach list 2 to the end of list 1: ')
linked_list.traverse()


print("Max value:", linked_list.max())
print("Min value:", linked_list.min())
print("Sum:", linked_list.sum())
print("Average:", linked_list.avg())
print("Is Sorted?", linked_list.sorted())

linked_list.insert(1)
print('list after insert 1 and sort is: ')
linked_list.traverse()

