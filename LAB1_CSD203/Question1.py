class SinglyLinkedList:

    class _Node:
        def __init__(self, value):
            self._value = value
            self._next = None

    def __init__(self):
        self._head = None
    
    def addToHead(self, x):
        new_node= self._Node(x)
        new_node._next = self._head
        self._head = new_node
        
    def addToTail(self, x):
        new_node = self._Node(x)
        if not self._head:
            self._head = new_node
            return
        current = self._head
        while current._next:
            current = current._next
        current._next = new_node
        
    def addAfter(self, p, x):
        new_node = self._Node(x)
        current = self.search(p)
        if current:
            new_node._next = current._next
            current._next = new_node
        else:
            print('Node not found')
    
    def traverse(self):
        current = self._head
        if not current:
            print('This list is Empty')
        while current:
            print(current._value, end = '->')
            current = current._next
        print(None)
    
    def deleteFromHead(self):
        if not self._head:
            print('List is empty')
            return None
        else:
            value = self._head._value
            self._head = self._head._next
            return value

    def deleteFromTail(self):
        if not self._head:
            print('List is empty')
            return None
        if not self._head._next:
            value = self._head._value
            self._head =  None
            return value
        current = self._head
        before = self._head 
        while current._next:
            before = current
            current = current._next
        value = current._value
        before._next = None
        return value
    
    def deleteAfter(self, p):
        current = self.search(p)
        if current and current._next:
            value = current._next._value
            current._next = current._next._next
            print('Value of node has been delete is: ',value)
        else:
            print('Node not found')
        
    def del_f(self,x):
        current = self._head
        if current and current._value == x:
            self._head = current._next
            return x 
        while current._next and current._next._value != x:
            current = current._next
        if current._next:
            value = current._next
            current._next = current._next._next
            return value
        else:
            print('Node not found')
        
    def search(self,x):
        current = self._head
        while current and current._value != x:
            current = current._next
        return current
    
    def count(self):
        current = self._head
        count = 0
        while current:
            current = current._next
            count += 1
        return count 
    
    def del_i(self, i):
        current = self._head
        if i == 0 :
           return self.deleteFromHead()
        else:
            for j in range(i-1):
                if current:
                    current = current._next
                else:
                    print('Invalid Index')
        if current and current._next:
            current._next = current._next._next
        else:
            print('Invalid Index')  

    def sort(self):
        current  = self._head
        if not current:
            print('List is empty') 
        else:
            values = self.toArray()
            values.sort()
            self._head = None
            for value in values:
                self.addToTail(value)

    def dele(self,p):
        current = self._head

        while current and current._value == p:
            self._head = current._next
            current = self._head

        while current and current._next:
            if current._next._value == p:
                current._next = current._next._next
            else:
                current = current._next
        return
    def toArray(self):
        result = []
        current = self._head
        while current:
            tmp = current._value
            result.append(tmp)
            current = current._next
        return result
    
    def merge(self, other_list):
        if not self._head:
            self._head = other_list
            return
        if not other_list._head:
            return
        current = self._head
        while current._next:
            current = current._next
        current._next = other_list._head

    def addBefore(self, p, x):
        current = self._head
        if not current:
            print('Node not found')
        if current._value == p:
            new_node = self._Node(x)
            new_node._next = current
            self._head = new_node
            return 
        
        while current._next and current._next._value != p :
            current = current._next

        if current._next:
            new_node = self._Node(x)
            new_node._next = current._next
            current._next = new_node
        else:
            print('Node not found')
        
    def attach(self, other_list):
        current = self._head
        if not self._head:
            self._head = other_list
            return 
        else:
            while current._next:
                current = current._next
            current._next = other_list._head
    
    def max(self):
        if not self._head:
            print('list is empty')
            return None
        
        max = self._head._value
        current = self._head._next
        while current:
            if current._value > max :
                max = current._value
            current = current._next
        return max

    def min(self):
        if not self._head:
            print("List is empty.")
            return None
        
        min = self._head._value
        current = self._head._next
        while current:
            if current._value < min:
                min = current._value
            current = current._next
        return min
    
    def sum(self):
        if not self._head:
            print("List is empty.")
            return None
        current = self._head
        sum = 0 
        while current:
            sum += current._value
            current = current._next
        return sum 
    
    def avg(self):
        total = self.sum()
        count = self.count()
        if count == 0:
            return 0
        else:
            return total/count
    
    def sorted(self):
        current = self._head
        while current and current._next:
            if current._value > current._next._value:
                return False
            current = current._next
        return True

    def insert(self, x):
        new_node = self._Node(x)
        self.addToTail(x)
        self.sort()


    def reverse(self):
        prev = None
        current = self._head
        while current:
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node
        self._head = prev
    
    def isEqual(self, other_list):
        current_self = self._head
        current_other = other_list._head
        while current_self and current_other:
            if current_self._value != current_other._value:
                return False
            current_self = current_self._next
            current_other = current_other._next
        if current_self or current_other:
            return False
        return True
    
    def display(self):
        current = self._head
        while  current:
            print(current._value, end = ' ')
            current = current._next
        print('\n')
    
if __name__ == '__main__':
    #CREATE A LINKED LIST WITH SOME GIVEN VALUE:
    linked_list = SinglyLinkedList()
    linked_list.addToTail(4)
    linked_list.addToTail(5)
    linked_list.addToTail(6)
    linked_list.addToTail(4)
    linked_list.addToTail(5)
    linked_list.addToTail(6)
    print('Original singly linked list: ')
    linked_list.display()

    # ADD 3 TO TAIL:
    linked_list.addToTail(7)
    print('After add 7 to Tail:')
    linked_list.display()
    
    # ADD 1 TO HEAD:
    linked_list.addToHead(1)
    print('After add 1 to Head:')
    linked_list.display()

    # ADD 2 AFTER 1:
    linked_list.addAfter(1,2)
    print('After add 2 after 1:')
    linked_list.display()

    # TRAVERSE:
    print('Traverse linked list: ')
    linked_list.traverse()

    # DELETE FROM HEAD:
    linked_list.deleteFromHead()
    print('After delete element at the Head: ')
    linked_list.display()

    # DELETE FROM TAIL 
    linked_list.deleteFromTail()
    print('After delete element at the Tail: ')
    linked_list.display()

    # DELETE NODE AFTER P AND RETURN ITS VALUE
    linked_list.deleteAfter(2)
    print('List after delete element after 2: ')
    linked_list.display()

    # DELETE NODE FIRST NODE HAS VALUE X:
    linked_list.del_f(5)
    print('After delete first element has value 5: ')
    linked_list.display()

    # COUNT ELEMENT IN LIST:
    print('Number element in list is: ',linked_list.count())

    # DELETE ELEMENT i-TH IN LIST:
    linked_list.del_i(1)
    print('After delete 1-th element: ')
    linked_list.display()
    
    # SORT LIST BY ASCENDING ORDER:
    linked_list.sort()
    print('After sort by ascending order: ')
    linked_list.display()
    
    # DELETE NODE P IF IT EXIST:
    linked_list.dele(2)
    print('After delete node has value 2: ')
    linked_list.display()

    # CREATE ARRAY CONTAIN ALL NODES' INFOR 
    print('''Array contain all nodes' infor is:\n''',linked_list.toArray())

    # MERGE TO ORDER LINKED LIST INTO ONE:
    linked_list_2 = SinglyLinkedList()
    linked_list_2.addToTail(1)
    linked_list_2.addToTail(7)
    linked_list_2.addToTail(8)
    print('Two original ordered list:')
    linked_list.display()
    linked_list_2.display()
    linked_list.merge(linked_list_2)
    print('After merger: ')
    linked_list.sort()
    linked_list.display()

    # ADD A NODE BEFORE NODE P:
    linked_list.addBefore(8,9)
    print('Linked list after add 9 before 8: ')
    linked_list.display()

    # ATTACH OTHER LINKED LIST AT THE END OF LINKED LIST:
    print('Two original linked lists: ')
    linked_list.display()
    linked_list_2.display()
    linked_list.attach(linked_list_2)
    print('After add linked list 2 at the end of linked list 1: ')
    linked_list.display()

    # FIND MAX:
    print('Max value of linked list is: ',linked_list.max())

    # FIND MIN:
    print('Min value of linked list is: ',linked_list.min())

    # CALCULATE SUM:
    print('Sum of all value of linked list is: ',linked_list.sum())

    # CALCULATE AVERAGE:
    print('Average value of linked list is: ',linked_list.avg())

    # CHECK IF LINKED LIST IS SORT OR NOT:
    print('CHECK LIST IS SORTED OR NOT: ')
    print('Is list is sorted: ',linked_list.sorted())

    # INSERT X AND SORT LIST:
    linked_list.addToTail(15)
    print('Linked list after add 15 and sort is: ')
    linked_list.sort()
    linked_list.display()

    # REVERSE ORDER OF LIST:
    linked_list.reverse()
    print('Linked list after reverse order: ')
    linked_list.display()

    # CHECK WHEATHER TWO LIST HAVE SAME CONTENT:
    print('Two linked lists are: ')
    linked_list.display()
    linked_list_2.display()
    print('Are two linked lists have same content: ',end = '')
    print(linked_list.isEqual(linked_list_2))






