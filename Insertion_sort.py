# Iterative
def iisort(A):
  n = len(A)
  if n < 1:
    return A
  for i in range(n):
    j = i
    while ((j > 0) and (A[j] < A[j-1])):
      (A[j], A[j-1]) = (A[j-1], A[j])
      j = j - 1
  return A


# Recurive 
# Both of the below functions are part of recursive insertion sort
def insert(A, e):
  n = len(A)
  if n == 0:
    return [e]
  elif e > A[-1]:
    return A + [e]
  else:
    return insert(A[:-1], e) + A[-1:]

def risort(A):
  n = len(A)
  if n < 1:
    return A
  else:
    return insert(risort(A[:-1]), A[-1])
