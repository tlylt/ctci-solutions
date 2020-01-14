# Delete the given nonterminal node from the containing linked list.
# Only access is to the middle node

import unittest

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

# Copy the data from next node to current node
# This will not work if node to be deleted is at the end
# can consider making it a dummy if it is the last node
def delete_middle(node):
  node.data = node.next.data
  node.next = node.next.next

class Test(unittest.TestCase):
  def test_delete_middle(self):
    head = Node(1,Node(2,Node(3,Node(4))))
    delete_middle(head.next.next)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 2)
    self.assertEqual(head.next.next.data, 4)

if __name__ == "__main__":
  unittest.main()
