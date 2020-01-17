# Implement a class that acts as a single stack made out of multiple stacks
# which each have a set capacity.

class MultiStack_1():
  def __init__(self,capacity):
    self.container = [] # main storage area
    self.capacity = capacity # specify number per stack

  def push(self,item):
    if not self.container or len(self.container[-1]) == self.capacity: # if there is nothing yet or current stack is full
      self.container.append([item]) # adding a new "stack" represented by list
    else:
      self.container[-1].append(item) # else just add the item into the current stack
  
  def pop(self):
    if not self.container:
      return None
    item = self.container[-1].pop()
    if len(self.container[-1]) == 0: # if current stack becomes empty after poping, remove that stack
      self.container.pop()
    return item
  
  def pop_at(self,stack_num):
    if len(self.container)<= stack_num: # check if stack number is reasonable
      return None
    item = self.container[stack_num].pop()
    if len(self.container[stack_num]) == 0: # if that stack becomes empty, pop it off
      self.container.pop(stack_num)
    return item

####################################################################################

class MultiStack():
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []
  
  def push(self, item):
    if len(self.stacks) and (len(self.stacks[-1]) < self.capacity):
      self.stacks[-1].append(item)
    else:
      self.stacks.append([item])
  
  def pop(self):
    while len(self.stacks) and (len(self.stacks[-1]) == 0):
      self.stacks.pop()
    if len(self.stacks) == 0:
      return None
    item = self.stacks[-1].pop()
    if len(self.stacks[-1]) == 0:
      self.stacks.pop()
    return item
  
  def pop_at(self, stack_number):
    if (stack_number < 0) or (len(self.stacks) <= stack_number):
      return None
    if len(self.stacks[stack_number]) == 0:
      return None
    return self.stacks[stack_number].pop()

import unittest

class Test(unittest.TestCase):
  def test_multi_stack(self):
    stack = MultiStack(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    self.assertEqual(stack.pop(), 88)
    self.assertEqual(stack.pop_at(1), 66)
    self.assertEqual(stack.pop_at(0), 33)
    self.assertEqual(stack.pop_at(1), 55)
    self.assertEqual(stack.pop_at(1), 44)
    self.assertEqual(stack.pop_at(1), None)
    stack.push(99)
    self.assertEqual(stack.pop(), 99)
    self.assertEqual(stack.pop(), 77)
    self.assertEqual(stack.pop(), 22)
    self.assertEqual(stack.pop(), 11)
    self.assertEqual(stack.pop(), None)
  def test_multi_stack_1(self):
    stack = MultiStack_1(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    self.assertEqual(stack.pop(), 88)
    self.assertEqual(stack.pop_at(1), 66)
    self.assertEqual(stack.pop_at(0), 33)
    self.assertEqual(stack.pop_at(1), 55)
    self.assertEqual(stack.pop_at(1), 44)
    self.assertEqual(stack.pop_at(1), 77)
    stack.push(99)
    self.assertEqual(stack.pop(), 99)
    self.assertEqual(stack.pop(), 22)
    self.assertEqual(stack.pop(), 11)
    self.assertEqual(stack.pop(), None)

if __name__ == "__main__":
  unittest.main()


