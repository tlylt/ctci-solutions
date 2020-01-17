# Sort a stack with the smallest on top using only a single temporary stack.

def sort_stack_1(stack):
  ordered_stack = Stack_1() # setting up another stack
  ordered_stack.push(stack.pop()) # push item from original stack 
  while not stack.is_empty(): 
    temp = stack.pop() # store item to be compared
    count = 0
    while ordered_stack.peek() != None: 
      if temp >= ordered_stack.peek():
        break
      count += 1
      stack.push(ordered_stack.pop()) # if items on ordered stack are bigger, push to original stack first
    ordered_stack.push(temp) # add item into ordered stack
    for _ in range(count):
      ordered_stack.push(stack.pop()) # restore those moved items back into ordered stack
  return ordered_stack

class Stack_1():
  def __init__(self):
    self.container = []

  def push(self,item):
    self.container.append(item)
  
  def pop(self):
    if self.container:
      return self.container.pop()
    return None
  def peek(self):
    if self.container:
      return self.container[-1]
    return None
  def is_empty(self):
    return self.container == []

#########################################################

def sort_stack(stack):
  temp = Stack()
  previous = stack.pop()
  current = stack.pop()
  while current:
    if current < previous:
      temp.push(current)
    else:
      temp.push(previous)
      previous = current
    current = stack.pop()
  is_sorted = True
  current = temp.pop()
  while current:
    if current > previous:
      is_sorted = False
      stack.push(current)
    else:
      stack.push(previous)
      previous = current
    current = temp.pop()
  stack.push(previous)
  if is_sorted:
    return stack
  return sort_stack(stack)

class Stack():
  def __init__(self):
    self.top = None
  
  def __str__(self):
    return str(self.top)
  
  def push(self, item):
    self.top = current(item, self.top)
  
  def pop(self):
    if not self.top:
      return None
    item = self.top
    self.top = self.top.next
    return item.data

class current():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    return str(self and self.data) + ',' + str(self and self.next)

import unittest

class Test(unittest.TestCase):
  def test_sort_stack(self):
    self.assertEqual(str(sort_stack(Stack())), "None,None")
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(70)
    stack.push(40)
    stack.push(80)
    stack.push(20)
    stack.push(90)
    stack.push(50)
    stack.push(60)
    self.assertEqual(str(stack), "60,50,90,20,80,40,70,30,10,None")
    self.assertEqual(str(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")

if __name__ == "__main__":
  # unittest.main()
  stack = Stack_1()
  stack.push(10)
  stack.push(30)
  stack.push(70)
  stack.push(40)
  stack.push(80)
  stack.push(20)
  sorted_stack = sort_stack_1(stack)
  while( not sorted_stack.is_empty()):
    print(sorted_stack.pop())
