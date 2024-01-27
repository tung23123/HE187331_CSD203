#!/usr/bin/env python
# coding: utf-8

# In[3]:


# QUESTION 1
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
print(sum(5))
print(sum(7))


# In[12]:


# QUESTION 2

def find_min(lst,n):
    if n == 1:
        return lst[0]
    return min(lst[n-1], find_min(lst, n-1))
print(find_min([10,5,3,2,4,6,1], 7))


# In[13]:


# QUESTION 3
def cal_sum(lst,n):
    if n == 1:
        return lst[0]
    return lst[n-1] + cal_sum(lst, n-1)
    
print(cal_sum([1,2,3,4,5,6], 6))


# In[79]:


# QUESTION 4 
def is_palindrome(lst, n):
    if n==0 or n==1:
        return True
    else:
        if (lst[0] == lst[-1]) and (is_palindrome(lst[1:-1], n-2)): return 1
        else:
            return 0

print(is_palindrome([1,1,2,3,3,1,1], 7))

print(is_palindrome([1,9,9,1], 4))


# In[83]:


# QUESTION 5:
def binary_search(lst, l, r, target):
    mid = (l+r) // 2
    if lst[mid] == target:
        print(f'{target} found at position {mid}')
        return
    
    elif lst[mid] > target:
        binary_search(lst, l, mid-1, target)
        
    else:
        binary_search(lst, mid+1 , r, target)
        
binary_search([1,2,3,4,5,6,7],0, 6, 5)

binary_search([2,4,6,7,10,25,66,115],0, 7, 4)


# In[87]:


# QUESTION 6:
def GCD(m,n):
    if n == 0:
        return m
    else:
        return GCD(n, m%n)
GCD(8,6)


# In[88]:


# QUESTION 7:
def power(x,n):
    if n == 0:
        return 1
    else:
        return x* power(x, n-1)
power(2,3)


# In[89]:


# QUESTION 8:
def fact(n):
    if n <= 1:
        return 1
    else:
        return n* fact(n-1)
fact(5)


# In[90]:


# QUESTION 9:
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
fib(5)


# In[91]:


# QUESTION 10:
def addReciprocals(n):
    if n == 1:
        return 1
    else:
        return 1/n + addReciprocals(n-1)
addReciprocals(10)


# In[6]:


# QUESTION 12 and 13
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    
    left_h = height(node.left)
    right_h = height(node.right)
    
    return 1 + max(left_h, right_h)

def size(node):
    if node is None:
        return 0
    
    left_s = size(node.left)
    right_s = size(node.right)
    
    return 1 + left_s + right_s


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

height = height(root)
print(f'The height of the binary tree is: {height}')

size = size(root)
print(f'The size of the binary tree is: {size}')

