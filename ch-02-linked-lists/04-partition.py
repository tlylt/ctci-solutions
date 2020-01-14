# Partition a linked list so that all of the nodes containing values less than
# a pivot value occur before all of the nodes containing values greater than
# or equal to the pivot value.

import unittest

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

# For stable solution (preserve order)
# make two lists, one will contain values smaller than pivot and the other will
# contain values equal or bigger, then merge then together
def partition_1(head, pivot):
  a_head, a_tail = None, None
  b_head, b_tail = None, None
  node = head
  while node:
    if node.data < pivot:
      if a_head: # update tail
        a_tail.next = node
        a_tail = node
      else:
        a_head, a_tail = node, node # setting up list one for the first time
    else:
      if b_head: # update tail
        b_tail.next, b_tail = node, node
      else: # setting up list two for the first time
        b_head, b_tail = node, node
    node = node.next
  a_tail.next = b_head # merge list one with list two
  return a_head

# For non order preserving 
# adding node smaller than pivot at the head, adding node bigger than pivot at the tail
def partition_2(head, pivot):
  new_head,tail = head, head
  curr = head
  while curr:
    next_node = curr.next
    if curr.data < pivot: # point node's next pointer to head and and make it the new head
      curr.next = new_head
      new_head = curr
    else:
      tail.next = curr # point tail's next pointer to node and make it the new tail
      tail = curr
    curr = next_node
  tail.next = None
  return new_head

class Test(unittest.TestCase):
  def test_partition_1(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition_1(head1, 6)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = partition_1(head2, 7)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")
  def test_partition_2(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition_2(head1, 6)
    self.assertEqual(str(head2), "3,1,2,7,9,6,8")
    head3 = partition_2(head2, 7)
    self.assertEqual(str(head3), "6,2,1,3,7,9,8")

if __name__ == "__main__":
  unittest.main()

