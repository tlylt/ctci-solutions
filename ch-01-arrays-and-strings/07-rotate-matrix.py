# Rotate a square matrix by 90 degrees clockwise about its center.

import unittest

# By swapping row by row
### Time: O(n2)
### Space: O(n)
def rotate_matrix(m):
  n = len(m)
  ans_matrix = [None] * n
  for i in range(n): # build new empty matrix
    ans_matrix[i] = [None] * n
  for row in range(n):
    for col in range(n):
      ans_matrix[n-1-col][row] = m[row][col]
  return ans_matrix

# By swapping index by index (four-way edge swap)
### Time: O(n2)
### Space: O(1)
def rotate_matrix_in_place(m):
  n = len(m)
  for layer in range(n//2):
    first = layer
    last = n - 1 - layer
    for i in range(first,last):
      offset = i - first
      top = m[first][i] #save top
      m[first][i] = m[last-offset][first] #set top left to bottom left
      m[last-offset][first] = m[last][last-offset] #set bottom left to bottom right
      m[last][last-offset] = m[i][last] #set bottom right to top right
      m[i][last] = top #set top right to top left
  return m

class Test(unittest.TestCase):
  def test_rotate_matrix(self):
    mat1 = [[1,2],[3,4]]
    mat2 = [[3,1],[4,2]]
  
  def test_rotate_matrix_in_place(self):
    mat1 = [[1,2],[3,4]]
    mat2 = [[3,1],[4,2]]
    rotate_matrix_in_place(mat1)
    self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()
