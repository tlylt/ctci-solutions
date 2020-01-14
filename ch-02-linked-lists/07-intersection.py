# Return an intersecting node if two linked lists intersect.

# 1.Run through each linked list to get the lengths and the tails
# 2.Compare the tails. If they are different, return immediately
# 3.Set two pointers to the start of each linked list
# 4.On the longer linked list, advance its pointer by the difference in lengths
# 5.Traverse on each linked list until the pointers are the same

import unittest

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

# By dictionary
### Time: O(n)
### Space: O(n)
def intersection_1(head1, head2):
  nodes = {}
  node = head1
  while node:
    nodes[node] = True
    node = node.next
  node = head2
  while node:
    if node in nodes:
      return node
    node = node.next
  return None

# For without dictionary
### Time: O(A + B)
### Space: O(1)
def intersection_2(head1,head2):
  if not head1 or not head2:
    return None
  len1,tail1 = 0,None
  len2,tail2 = 0,None
  curr1,curr2 = head1,head2
  while curr1.next:
    len1+=1
    tail1=curr1
    curr1 = curr1.next
  while curr2.next:
    len2+=1
    tail2=curr2
    curr2 = curr2.next
  if tail1 != tail2:
    return None
  if len1>len2:
    longer,shorter = head1,head2
  else:
    longer,shorter = head2,head1
  for _ in range(abs(len1-len2)):
    longer=longer.next
  while longer != shorter:
    longer=longer.next
    shorter=shorter.next
  return longer

class Test(unittest.TestCase):
  def test_intersection_1(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection_1(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection_1(head3, head4), node)
  def test_intersection_2(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection_2(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection_2(head3, head4), node)


if __name__ == "__main__":
  unittest.main()

