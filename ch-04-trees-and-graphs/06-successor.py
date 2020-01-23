# Return the successor of a node in a binary search tree.

# Pseudocode
# def function(node):
#  if node has right subtree
#     return leftmost of the right subtree
#  while node is a right child
#     node = node.parent
#  node is a left child, next node is the parent node


def successor(node):
  if not node:
    return None
  child = node.right
  if child: #if there is right subtree
    while child.left:
      child = child.left # find the leftmost child of right subtree
    return child
  while node.parent and node.parent.left != node: # if there is actually parent node
    node = node.parent # traverse up until node is not a right child
  return node.parent

class Node():
  def __init__(self, data, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.parent = None
    if self.left:  self.left.parent  = self
    if self.right: self.right.parent = self

import unittest

class Test(unittest.TestCase):
  def test_successor(self):
    self.assertEqual(successor(Node(22, Node(11))), None)
    self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
    self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)

if __name__ == "__main__":
  unittest.main()

