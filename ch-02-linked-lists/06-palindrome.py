# Determine whether or not a linked list is a palindrome.

import unittest

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

# By stack 
### Time: O(n)
### Space: O(n)
def is_palindrome_1(head):
  ref = []
  curr = head
  while curr: # load the data into a list
    ref.append(curr.data)
    curr = curr.next
  check = head
  while ref: # pops and check the linked list
    if check.data != ref[-1]: 
      return False
    check=check.next
    ref=ref[:-1]
  return True

# By stack, taking only first half and compare the reversed of it to second half
### Time: O(n)
### Space: O(n)
def is_palindrome_2(head):
  ref = []
  fast,slow = head,head
  while fast and fast.next:
    ref.append(slow.data)
    fast = fast.next.next
    slow = slow.next
  if fast:
    slow = slow.next # if list has odd number, start comparing at the next node, ignore middle
  while slow:
    val = ref.pop()
    if val !=slow.data:
      return False
    slow=slow.next
  return True

def is_palindrome_3(head):
  forward, backward = head, copy_reverse(head)
  while forward:
    if forward.data != backward.data:
      return False
    forward, backward = forward.next, backward.next
  return True

def copy_reverse(head):
  prev = None
  node = copy(head)
  while node:
    next = node.next
    node.next = prev
    prev = node
    node = copy(next)
  return prev

def copy(node):
  if node:
    return Node(node.data, node.next)
  else:
    return None

class Test(unittest.TestCase):
  def test_palindrome_1(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome_1(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome_1(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome_1(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome_1(list4))    
  def test_palindrome_2(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome_2(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome_2(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome_2(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome_2(list4))  
  def test_palindrome_3(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome_3(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome_3(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome_3(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome_3(list4))
  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(copy_reverse(head)), "40,30,20,10")

if __name__ == "__main__":
  unittest.main()

