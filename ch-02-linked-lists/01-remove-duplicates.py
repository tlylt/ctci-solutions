# Remove the duplicate values from a linked list.
# Follow up: No Buffer Allowed

import unittest

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

# By dictionary
### Time: O(n)
### Space: O(n)
def remove_duplicates_1(head):
  node = head
  if node:
    values = {node.data: True}
    while node.next:
      if node.next.data in values:
        node.next = node.next.next
      else:
        values[node.next.data] = True
        node = node.next
  return head

# By array
### Time: O(n)
### Space: O(n)
def remove_duplicates_2(head):
  ref = []
  prev = None
  curr = head
  while curr.next:
    if curr.data in ref:
      prev.next = curr.next
    else:
      ref.append(curr.data)
      prev = curr
    curr = curr.next
  return head

# Follow up, by two pointers
### Time: O(n2)
### Space: O(1)
def remove_duplicates_3(head):
  curr = head
  while curr.next:
    runner = curr
    while runner.next:
      if runner.next.data == curr.data:
        runner.next = runner.next.next
      else:
        runner = runner.next
    curr = curr.next
  return head

class Test(unittest.TestCase):
  def test_remove_duplicates_1(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates_1(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)
  def test_remove_duplicates_2(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates_2(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)
  def test_remove_duplicates_3(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates_3(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
  unittest.main()

