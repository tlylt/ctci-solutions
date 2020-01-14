# Given a matrix, zero out every row and column that contains a zero.

import unittest

# By flag out zero positions
### Time: O(MN)
### Space: O(MN)
def zero_out_row_col_1(mat):
  to_zero_out = []
  row = len(mat)
  col = len(mat[0])
  for n in range(row):
    for m in range(col):
      if mat[n][m] == 0:
        to_zero_out.append((n,m))
  for n,m in to_zero_out:
    for i in range(row):
      mat[i][m] = 0
    for x in range(col):
      mat[n][x] = 0
  return mat

# By recording in place using first col and first row
### Time: O(MN)
### Space: O(1)
def zero_out_row_col_2(mat):
  first_row_has_zero = False
  first_col_has_zero = False
  n_row = len(mat)
  n_col = len(mat[0])
  #check if first row has zero
  for i in range(n_col):
    if mat[0][i] == 0:
      first_row_has_zero = True
      break

  #check if first column has zero
  for i in range(n_row):
    if mat[i][0] == 0:
      first_col_has_zero = True
      break
  
  #check for zeros in the rest of the array
  for i in range(1,n_row):
    for j in range(1,n_col):
      if mat[i][j] == 0:
        mat[0][j] = 0
        mat[i][0] = 0
  
  #nullify based on first column
  for i in range(1,n_row):
    if mat[i][0] == 0:
      for x in range(n_col):
        mat[i][x] = 0

  #nullify based on first row
  for i in range(1,n_col):
    if mat[0][i] == 0:
      for x in range(n_col):
        mat[x][i] = 0
  
  #nullify first column if necessary
  if first_col_has_zero:
    for i in range(n_row):
      mat[i][0] = 0

  #nullify first row if necessary
  if first_row_has_zero:
    for i in range(n_col):
      mat[0][i] = 0

  return mat

class Test(unittest.TestCase):
  def test_zero_out_row_col_matrix(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zero_out_row_col_1(mat1)
    self.assertEqual(mat1, mat2)
  def test_zero_out_row_col_matrix_in_place(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zero_out_row_col_2(mat1)
    self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()
