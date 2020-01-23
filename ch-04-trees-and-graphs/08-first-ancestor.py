# Find the first common ancestor of two nodes in a tree.

def first_common_ancestor(node1, node2):
  search1, search2 = node1, node2
  ancestors1, ancestors2 = {}, {} # for record
  while search1 or search2: # while there is still node
    if search1:
      if search1 in ancestors2: # if node1's parent has been seen in node2's ancestor tree
        return search1
      ancestors1[search1] = True # add node1 to node1's ancestor tree
      search1 = search1.parent # traverse upwards
    if search2:
      if search2 in ancestors1: 
        return search2
      ancestors2[search2] = True
      search2 = search2.parent
  return None

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.parent = None
    if self.left:
      self.left.parent = self
    if self.right:
      self.right.parent = self

import unittest

class Test(unittest.TestCase):
  def test_first_common_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    self.assertEqual(first_common_ancestor(node1, node2), None)
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    self.assertEqual(first_common_ancestor(node1, node2), node3)

if __name__ == "__main__":
  unittest.main()
