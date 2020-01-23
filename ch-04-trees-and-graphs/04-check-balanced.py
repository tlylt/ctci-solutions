# Tell whether or not a binary tree is balanced.

def is_balanced_1(root):
  if check_height(root) == -1:
    return False
  return True

def check_height(root):
  if root == None:
    return 0 # height of 0
  
  left_height = check_height(root.left) # check if left is balanced
  if left_height == -1:
    return -1 # not balanced
  
  right_height = check_height(root.right) # check if right is balanced
  if right_height == -1:
    return -1 # not balanced

  height_diff = abs(left_height - right_height)
  if height_diff > 1:
    return -1 # not balanced
  else:
    return max(left_height,right_height) + 1 # return height
  # if a node has no children, it will return 1
  # if a node has one or two children, it will return 2 

####################################################################

def is_balanced(binary_tree):
  if not binary_tree:
    return (True, 0)
  (left_balanced,  left_depth)  = is_balanced(binary_tree.left) # check on left side
  if not left_balanced:
    return (False, None)
  (right_balanced, right_depth) = is_balanced(binary_tree.right) # check on right side
  if (not right_balanced) or (abs(left_depth - right_depth) > 1):
    return (False, None)
  depth = max(left_depth, right_depth) + 1
  return (True, depth)

class Node():
  def __init__(self, left=None, right=None):
    self.left, self.right = left, right

import unittest

class Test(unittest.TestCase):
  def test_is_balanced(self):
    self.assertEqual(is_balanced(Node(Node(),Node())), (True, 2))
    self.assertEqual(is_balanced(Node(Node(),Node(Node()))), (True, 3))
    self.assertEqual(is_balanced(Node(Node(),Node(Node(Node())))),
        (False, None))
    self.assertEqual(is_balanced(Node(Node(Node()),Node(Node(Node())))),
        (False,None))
    self.assertEqual(is_balanced(Node(Node(Node()),
        Node(Node(Node()),Node()))), (True, 4))
  def test_is_balanced_1(self):
    self.assertEqual(is_balanced_1(Node(Node(),Node())), (True))
    self.assertEqual(is_balanced_1(Node(Node(),Node(Node()))), (True))
    self.assertEqual(is_balanced_1(Node(Node(),Node(Node(Node())))),
        (False))
    self.assertEqual(is_balanced_1(Node(Node(Node()),Node(Node(Node())))),
        (False))
    self.assertEqual(is_balanced_1(Node(Node(Node()),
        Node(Node(Node()),Node()))), (True))
if __name__ == "__main__":
  unittest.main()
