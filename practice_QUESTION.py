#QUESTION 1:
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            raise Exception("EmptyStackException: Stack is empty")
        return self.items.pop()

    def top(self):
        if self.isEmpty():
            raise Exception("EmptyStackException: Stack is empty")
        return self.items[-1]

    def traverse(self):
        traverse = [item for item in reversed(self.items)]
        return traverse

def decimal_to_binary(decimal_num):
    stack = Stack()
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num //= 2

    binary_result = ""
    while not stack.isEmpty():
        binary_result += str(stack.pop())
    return binary_result


# FUNCTION TO TEST Q1 OPERATIONS:
def test_stack():
    stack = Stack()
    print("Is Stack Empty? ", stack.isEmpty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('Stack after push 10, 20, 30: ',stack.traverse(),'(NOTE: Stack traverse show items in order from TOP to BOTTOM)')

    print("Top of the Stack:", stack.top())
    
    pop = stack.pop()
    print("Popped Value:", pop)
    print('After pop: ',stack.traverse())

    stack.clear()
    print('Stack after clear:')
    print("Is Stack Empty?", stack.isEmpty())

print('-'*20+'QUESTION 1'+'-'*20)
decimal_number = 25
binary_result = decimal_to_binary(decimal_number)
print(f"{decimal_number} in binary: {binary_result}")
test_stack()


#QUESTION 2:
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("EmptyQueueException: Queue is empty")
        return self.items.pop(0)

    def first(self):
        if self.isEmpty():
            raise Exception("EmptyQueueException: Queue is empty")
        return self.items[0]

    def traverse(self):
        print("Queue:", self.items)

def real_to_binary(real_num):
    queue = Queue()
    frac = None
    while not frac == 0:
        tmp = real_num * 2
        queue.enqueue(int(tmp))
        frac = tmp % 1
        real_num = frac
        
    binary_result = ""
    while not queue.isEmpty():
        binary_result += str(queue.dequeue())
    return binary_result

# FUNCTION TO TEST Q2 OPERATIONS:
def test_queue_operations():
    queue = Queue()
    print("Is Queue Empty?", queue.isEmpty())

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print('Queue after enqueue 10, 20, 30 ')
    queue.traverse()

    print("First element in the Queue:", queue.first())
    dequeued_value = queue.dequeue()
    
    print("Dequeued Value:", dequeued_value)
    queue.traverse()

    queue.clear()
    print("After clear:\nIs Queue Empty?", queue.isEmpty())

print('\n\n'+'-'*20+'QUESTION 2'+'-'*20)
test_queue_operations()

real_number = 0.625
binary_result = real_to_binary(real_number)
print(f"{real_number} in binary: 0.{binary_result}")


def test_string():
    stack = Stack()
    queue = Queue()
    # TEST STACK STRING:
    stack = Stack()
    print('\n\n'+'-'*20+'QUESTION 3'+'-'*20)
    print("Is Stack Empty? ", stack.isEmpty())
    stack.push('CSD203')
    stack.push('LAB2')
    print('''Stack after push 'CSD203' and 'LAB2': ''',stack.traverse(),'(NOTE: Stack traverse show items in order from TOP to BOTTOM)')

    print("Top of the Stack:", stack.top())
    
    pop = stack.pop()
    print("Popped Value:", pop)
    print('After pop: ',stack.traverse())

    stack.clear()
    print('Stack after clear:')
    print("Is Stack Empty?", stack.isEmpty())
 

    #TEST QUEUE STRING
    print('\n')
    print('Is queue is empty:',queue.isEmpty())
    queue.enqueue('Apple')
    queue.enqueue('SamSung')
    queue.enqueue('XiaoMi')
    print('''Queue after enqueue 'Apple', 'SamSung', 'XiaoMi': ''')
    queue.traverse()

    print("First element in the Queue:", queue.first())
    dequeued_value = queue.dequeue()
    
    print("Dequeued Value:", dequeued_value)
    queue.traverse()

    queue.clear()
    print("After clear:\nIs Queue Empty?", queue.isEmpty())
    print('\n\n QUESTION 4: PYTHON KHÔNG CÓ CHARACTER TYPE ĐỀU LÀ STRING TYPE. CODE GIỐNG CÂU 3 NÊN EM BỎ QUA Ạ')
    

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def test_object():
    stack = Stack()
    queue = Queue()
    #TEST STACK
    print('\n\n'+'-'*20+'QUESTION 5'+'-'*20)
    print("Is Stack Empty? ", stack.isEmpty())
    stack.push(Computer("Macbook Air 13-inch").__str__())
    stack.push(Computer("DELL XPS 13").__str__())
    stack.push(Computer("ASUS ROG").__str__())
    print('Stack after add three more objects from computer class:(NOTE: Stack traverse show items in order from TOP to BOTTOM)')
    print(stack.traverse())
    
    print("Top of the Stack:", stack.top())

    pop = stack.pop()
    print("Popped Value:", pop)
    print('After pop: ',stack.traverse())

    stack.clear()
    print('Stack after clear:')
    print("Is Stack Empty?", stack.isEmpty())
 
    #TEST QUEUE
    print('\n')
    print('Is queue is empty:',queue.isEmpty())
    queue.enqueue(Computer("MacBook").__str__())
    queue.enqueue(Computer("PC").__str__())
    queue.enqueue(Computer("Workstation").__str__())
    print('Queue after add three more objects from computer class')
    print(queue.traverse())
    print("First element in the Queue:", queue.first())
    dequeued_value = queue.dequeue()
    
    print("Dequeued Value:", dequeued_value)
    queue.traverse()

    queue.clear()
    print("After clear:\nIs Queue Empty?", queue.isEmpty())

if __name__ == '__main__':
    test_string()
    test_object()