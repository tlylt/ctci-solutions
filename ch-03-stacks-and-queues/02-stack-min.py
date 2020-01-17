# Implement a stack with a function that returns the current minimum item.

class MinStack():
  def __init__(self):
    self.top, self._min = None, None
    
  def min(self):
    if not self._min:
      return None
    return self._min.data
    
  def push(self, item):
    if self._min and (self._min.data < item):
      self._min = Node(data=self._min.data, next=self._min)
    else:
      self._min = Node(data=item, next=self._min)
    self.top = Node(data=item, next=self.top)
  
  def pop(self):
    if not self.top:
      return None
    self._min = self._min.next
    item = self.top.data
    self.top = self.top.next
    return item

class Node():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

################################################################

class MinStack_1():
  def __init__(self):
    self.container = []
  
  def min(self):
    if self.container:
      return self.container[-1].local_min
    return None

  def push(self,data):
    curr_min = self.min()
    if not curr_min:
      curr_min = float('inf')
    min_val = min(data,curr_min)
    new_val = Node_1(data,min_val)
    self.container.append(new_val)

  def pop(self):
    if self.container:
      item = self.container.pop()
      return item.data
    return None

class Node_1():
  def __init__(self,data,min_val=None):
    self.data = data
    self.local_min = min_val

import unittest

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = MinStack()
    self.assertEqual(min_stack.min(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.min(), 7)
    min_stack.push(6)
    min_stack.push(5)
    self.assertEqual(min_stack.min(), 5)
    min_stack.push(10)
    self.assertEqual(min_stack.min(), 5)
    self.assertEqual(min_stack.pop(), 10)
    self.assertEqual(min_stack.pop(), 5)
    self.assertEqual(min_stack.min(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.min(), None)
  def test_min_stack_1(self):
    min_stack_1 = MinStack_1()
    self.assertEqual(min_stack_1.min(), None)
    min_stack_1.push(7)
    self.assertEqual(min_stack_1.min(), 7)
    min_stack_1.push(6)
    min_stack_1.push(5)
    self.assertEqual(min_stack_1.min(), 5)
    min_stack_1.push(10)
    self.assertEqual(min_stack_1.min(), 5)
    self.assertEqual(min_stack_1.pop(), 10)
    self.assertEqual(min_stack_1.pop(), 5)
    self.assertEqual(min_stack_1.min(), 6)
    self.assertEqual(min_stack_1.pop(), 6)
    self.assertEqual(min_stack_1.pop(), 7)
    self.assertEqual(min_stack_1.min(), None)

if __name__ == "__main__":
  unittest.main()

