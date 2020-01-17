# Use a single array to implement three stacks.

class ThreeStacks():
  def __init__(self):
    self.array = [None, None, None] # container that is going to take items like a stack
    self.current = [0, 1, 2] # pointer to the last position of each stack
  
  def push(self, item, stack_number):
    if not stack_number in [0, 1, 2]: # choose the stack
      raise Exception("Bad stack number")
    while len(self.array) <= self.current[stack_number]: # once size of current stack exceeds required
      self.array += [None] * len(self.array) # double the stack sizes
    self.array[self.current[stack_number]] = item # items in stack 0 is stored 2 items apart
    self.current[stack_number] += 3
  
  def pop(self, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    if self.current[stack_number] > 3: # if there is anything stored
      self.current[stack_number] -= 3 # goes back to the pointer to that thing
    item = self.array[self.current[stack_number]] # get the item
    self.array[self.current[stack_number]] = None # set the pointer to None
    return item

#############################################################################

class FourStacks():
  def __init__(self):
      self.container = [None] * 4 # actual place to put the items
      self.pointer = [0,1,2,3] # keep track of where each stack is at

  def push(self,item,stack_number):
    if not stack_number in [0,1,2,3]: # if not in stated stacks, raise error
      raise Exception("Bad stack number")
    if self.pointer[stack_number]>= len(self.container): #if pointer has moved and greater than length of container
      self.container+=([None]*len(self.container))
    self.container[self.pointer[stack_number]] = item
    self.pointer[stack_number]+=4

  def pop(self,stack_number):
    if not stack_number in [0,1,2,3]:
      raise Exception("Bad stack number")    
    if self.pointer[stack_number] >= 4: # if pointer has ever been moved ahead
      self.pointer[stack_number]-=4 # back one place
    item = self.container[self.pointer[stack_number]] # store the item as temp
    self.container[self.pointer[stack_number]] = None # set that place as None
    return item

import unittest

class Test(unittest.TestCase):
  def test_three_stacks(self):
    three_stacks = ThreeStacks()
    three_stacks.push(101, 0)
    three_stacks.push(102, 0)
    three_stacks.push(103, 0)
    three_stacks.push(201, 1)
    self.assertEqual(three_stacks.pop(0), 103)
    self.assertEqual(three_stacks.pop(1), 201)
    self.assertEqual(three_stacks.pop(1), None)
    self.assertEqual(three_stacks.pop(2), None)
    three_stacks.push(301, 2)
    three_stacks.push(302, 2)
    self.assertEqual(three_stacks.pop(2), 302)
    self.assertEqual(three_stacks.pop(2), 301)
    self.assertEqual(three_stacks.pop(2), None)
  def test_four_stacks(self):
    four_stacks = FourStacks()
    four_stacks.push(100, 0)
    four_stacks.push(110, 1)
    four_stacks.push(101, 0)
    four_stacks.push(102, 0)
    four_stacks.push(130, 3)
    self.assertEqual(four_stacks.pop(0),102)
    self.assertEqual(four_stacks.pop(0),101)
    self.assertEqual(four_stacks.pop(3),130)

if __name__ == "__main__":
  unittest.main()