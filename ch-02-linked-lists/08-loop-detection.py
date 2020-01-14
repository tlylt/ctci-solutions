# Detect whether or not a linked list contains a cycle.

# Detect if linked list has a loop
## Done by fast/slow runner approach, they will eventually collide 
## e.g. slow at spot i, fast at spot i+1, previously slow at i-1, fast at i-1
## fast will not completely hop over slow

# When do they collide
## When slow enters the looped portion after k steps, fast has taken 2k steps total and
## are 2k - k = k steps into the looped portion
## since k might be larger than the loop length, it should be mod(k, loop_size) = D steps into
## the looped portion. at each subsequent step, fast will get one step closer to slow.
## since fast is now loop_size - D steps behind slow, it takes loop_size - D steps for then to collide
## and they will collide at D steps before the head of the loop

# How do you find the start of the loop
## the collision spot is D steps before the start of the loop. Since D = mod(k, loop_size),
## k = D + M * loopsize for any integer M, hence the collision spot is also k steps before head
## of the loop. Hence both the collision spot and linkedlist head are k steps from head of loop.
## Keeping one pointer and move the other to start of linkedlist, when they move at same speed 
## and collide again, it will be at the start of the loop

import unittest

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

# By dictionary
def detect_cycle_1(head):
  nodes = {}
  node = head
  while node:
    if node in nodes:
      return node
    nodes[node] = True
    node = node.next
  return None

# By pattern matching approach
def detect_cycle_2(head):
  fast,slow = head,head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: # collide, at loop_size - k steps before the head
      break
  if not fast or not fast.next: # reaches the end, no collision, no loop
    return None 
  fast = head
  while fast != slow: 
    fast = fast.next
    slow = slow.next
  return fast

class Test(unittest.TestCase):
  def test_detect_cycle_1(self):
    head1 = Node(100,Node(200,Node(300)))
    self.assertEqual(detect_cycle_1(head1), None)
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    self.assertEqual(detect_cycle_1(head2), node1)
  def test_detect_cycle_2(self):
    head1 = Node(100,Node(200,Node(300)))
    self.assertEqual(detect_cycle_2(head1), None)
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    self.assertEqual(detect_cycle_2(head2), node1)

if __name__ == "__main__":
  unittest.main()
