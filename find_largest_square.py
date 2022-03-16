# http://leetcode.com/problems/maximal-square/
def solve(matrix):
  maxCount = 0
  # iterate over the matrix
  # for each cell check if it contains a 1, if it does, increase the size of the square and check again
  for rowIndex, row in enumerate(matrix):
    for valIndex, val in enumerate(row):
      maxColDim = len(matrix[0]) - valIndex
      maxRowDim = len(matrix) - rowIndex
      maxDim = maxColDim if maxColDim < maxRowDim else maxRowDim
      for i in range(maxDim):
        dim = i + 1
        if validateOuterEdges(matrix, rowIndex, valIndex, dim):
          count = dim * dim
          if (count > maxCount):
            maxCount = count
        else:
          break

  return maxCount

def validateArea(matrix, rowOffset, itemOffset, dim):
  for r in range(dim):
    for c in range(dim):
      cix = itemOffset + c
      rix = rowOffset + r
      if matrix[rix][cix] == 0:
        return False
  return True

def validateOuterEdges(matrix, rowOffset, itemOffset, dim):
  # check column
  for ro in range(dim):
    if matrix[rowOffset+ro][itemOffset+dim-1] == 0:
      return False
  # check row
  for co in range(dim):
    if matrix[rowOffset+dim-1][itemOffset+co] == 0:
      return False
  return True

if __name__ == '__main__':
  count = solve([
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
  ])
  print(f"expected 4 got {count}")

  count = solve([
    [1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1],
  ])
  print(f"expected 9 got {count}")

  count = solve([
    [0, 1],
    [1, 0],
  ])
  print(f"expected 1 got {count}")

  count = solve([
    [1, 0],
  ])
  print(f"expected 1 got {count}")
