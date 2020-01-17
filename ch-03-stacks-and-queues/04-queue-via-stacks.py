# Implement a queue using two stacks.

# By always maintain one stack

class Stack_1(): # typical stack implementation
  def __init__(self):
    self.container = []
  def __len__(self):
    return len(self.container)
  def push(self,data):
    self.container.append(data)
  def pop(self):
    if self.container:
      return self.container.pop()
    return None

class QueueViaStacks_1():
  def __init__(self):
    self.primary = Stack_1()
    self.axillary = Stack_1() # used for reversing

  def enqueue(self,data):
    self.primary.push(data)

  def dequeue(self):
    if self.primary:
      #check existence by length as it is a stack object, also need to specify len property
      while len(self.primary) > 0 : # reverse all items in primary and put into axillary
        self.axillary.push(self.primary.pop())
      item = self.axillary.pop() # get the first item for dequeue
      while len(self.axillary) > 0: # return items back to primary stack
        self.primary.push(self.axillary.pop()) 
      return item
    return None

# Lazy approach
class QueueViaStacks():
  def __init__(self):
    self.in_stack = Stack()
    self.out_stack = Stack()
  
  def add(self, item):
    self.in_stack.push(item)
    
  def remove(self):
    if len(self.out_stack) == 0: # if second stack has something
      while len(self.in_stack): # pop equals dequeue as this stack will have oldest item on top
        self.out_stack.push(self.in_stack.pop()) 
    return self.out_stack.pop() # if there is nothing, pop all items from in stack to out stack

class Stack():
  def __init__(self):
    self.array = []
  
  def __len__(self):
    return len(self.array)
  
  def push(self, item):
    self.array.append(item)
  
  def pop(self):
    if not len(self.array):
      return None
    return self.array.pop()

import unittest

class Test(unittest.TestCase):
  def test_queue_via_stacks(self):
    queue = QueueViaStacks()
    queue.add(11)
    queue.add(22)
    queue.add(33)
    self.assertEqual(queue.remove(), 11)
    queue.add(44)
    queue.add(55)
    queue.add(66)
    self.assertEqual(queue.remove(), 22)
    self.assertEqual(queue.remove(), 33)
    self.assertEqual(queue.remove(), 44)
    self.assertEqual(queue.remove(), 55)
    queue.add(77)
    self.assertEqual(queue.remove(), 66)
    self.assertEqual(queue.remove(), 77)
    self.assertEqual(queue.remove(), None)
  def test_queue_via_stacks_1(self):
    queue = QueueViaStacks_1()
    queue.enqueue(11)
    queue.enqueue(22)
    queue.enqueue(33)
    self.assertEqual(queue.dequeue(), 11)
    queue.enqueue(44)
    queue.enqueue(55)
    queue.enqueue(66)
    self.assertEqual(queue.dequeue(), 22)
    self.assertEqual(queue.dequeue(), 33)
    self.assertEqual(queue.dequeue(), 44)
    self.assertEqual(queue.dequeue(), 55)
    queue.enqueue(77)
    self.assertEqual(queue.dequeue(), 66)
    self.assertEqual(queue.dequeue(), 77)
    self.assertEqual(queue.dequeue(), None)
if __name__ == "__main__":
  unittest.main()

