# Determine whether or not a given string is a rotation of another string.

import unittest

# Rotation means there must be a rotation point where the string can be split
# into x and y and combined to be y and x. This leads to the fact that xyxy,
# which is string 1 + string 1 must contain yx which is a rotation

### Time: O(n) depending on runtime of function is_substring which likely O(A + B)
def is_rotation(s1, s2):
  if len(s1) != len(s2):
    return False
  return is_substring(s1 + s1, s2)

