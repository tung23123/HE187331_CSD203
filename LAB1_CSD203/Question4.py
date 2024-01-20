class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            new_node.next = new_node  # Point to itself in a circular list
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            new_node.next = new_node  # Point to itself in a circular list
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
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
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

    def deleteFromHead(self):
        if not self.head:
            print("List is empty.")
            return None
        deleted_data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        return deleted_data

    def deleteFromTail(self):
        if not self.head:
            print("List is empty.")
            return None
        deleted_data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            deleted_data = current.next.data
            current.next = self.head
        return deleted_data

    def deleteAfter(self, p):
        current = self.head
        while current and current.data != p:
            current = current.next
        if not current or current.next == self.head:
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
            return self.deleteFromHead()
        current = self.head
        while current.next != self.head and current.next.data != x:
            current = current.next
        if current.next == self.head:
            print(f"Node with value {x} not found.")
            return None
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def search(self, x):
        current = self.head
        while current and current.data != x:
            current = current.next
            if current == self.head:
                return None
        return current

    def count(self):
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def delAtIndex(self, i):
        if i <= 0:
            print("Invalid index.")
            return
        if i == 1:
            self.deleteFromHead()
            return
        current = self.head
        for _ in range(i - 2):
            current = current.next
            if current == self.head:
                print("Index out of bounds.")
                return
        current.next = current.next.next

    def sort(self):
        sorted_list = sorted(self.toArray())
        self.head = None
        for value in sorted_list:
            self.addToTail(value)

    def delNode(self, p):
        if not self.head:
            print("List is empty.")
            return None
        if self.head == p:
            return self.deleteFromHead()
        current = self.head
        while current.next != self.head and current.next != p:
            current = current.next
        if current.next == self.head:
            print(f"Node {p} not found.")
            return None
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def toArray(self):
        array = []
        current = self.head
        while True:
            array.append(current.data)
            current = current.next
            if current == self.head:
                break
        return array

    def mergeOrderedLists(self, other_list):
        merged_list = CircularLinkedList()
        current1 = self.head
        current2 = other_list.head

        while True:
            if current1.data < current2.data:
                merged_list.addToTail(current1.data)
                current1 = current1.next
            else:
                merged_list.addToTail(current2.data)
                current2 = current2.next

            if current1 == self.head:
                while current2 != other_list.head:
                    merged_list.addToTail(current2.data)
                    current2 = current2.next
                break

            if current2 == other_list.head:
                while current1 != self.head:
                    merged_list.addToTail(current1.data)
                    current1 = current1.next
                break

        return merged_list

    def addBefore(self, p, x):
        new_node = Node(x)
        current = self.head
        while current.next != self.head and current.next != p:
            current = current.next
        if current.next == self.head:
            print(f"Node {p} not found.")
            return
        new_node.next = current.next
        current.next = new_node

    def attachList(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = other_list.head
            return

    def max(self):
        if not self.head:
            return None
        max_val = self.head.data
        current = self.head.next
        while True:
            if current.data > max_val:
                max_val = current.data
            current = current.next
            if current == self.head:
                break
        return max_val

    def min(self):
        if not self.head:
            return None
        min_val = self.head.data
        current = self.head.next
        while True:
            if current.data < min_val:
                min_val = current.data
            current = current.next
            if current == self.head:
                break
        return min_val

    def sum(self):
        total = 0
        current = self.head
        while True:
            total += current.data
            current = current.next
            if current == self.head:
                break
        return total

    def avg(self):
        count = self.count()
        if count == 0:
            return None
        return self.sum() / count

    def sorted(self):
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def insert(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head and current.next.data < x:
            current = current.next
        new_node.next = current.next
        current.next = new_node


# Example usage:
circular_list = CircularLinkedList()
circular_list.addToHead(5)
print('List after add 5 to Head: ')
circular_list.traverse()
circular_list.addToTail(3)
circular_list.addToTail(7)
print('List after add 3, 7 to Tail: ')
circular_list.traverse()

circular_list.addAfter(3, 6)
print('List after add 6 after 3: ')
circular_list.traverse()

circular_list.deleteFromHead()
print('List after delete from Head: ')
circular_list.traverse()

circular_list.deleteFromTail()
print('List after delete from Tail: ')
circular_list.traverse()

circular_list.deleteAfter(3)
print('List after delete after 3: ')
circular_list.traverse()

circular_list.delNode(6)
print('List after delete node 6: ')
circular_list.traverse()

circular_list.sort()
print('List after sort: ')
circular_list.traverse()

print("Merged List:")
list1 = CircularLinkedList()
list1.addToTail(2)
list1.addToTail(4)
list1.addToTail(6)

list2 = CircularLinkedList()
list2.addToTail(1)
list2.addToTail(3)
list2.addToTail(5)
print('Two original list: ')
list1.traverse()
list2.traverse()

merged_list = list1.mergeOrderedLists(list2)
print('after merge: ')
merged_list.traverse()

circular_list.addBefore(7, 8)
print('List after add 8 before 7: ')
circular_list.traverse()

print("Max value:", circular_list.max())
print("Min value:", circular_list.min())
print("Sum:", circular_list.sum())
print("Average:", circular_list.avg())
print("Is Sorted?", circular_list.sorted())

circular_list.insert(1)
print('List after insert 1 and sort: ')
circular_list.traverse()
