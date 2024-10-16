# Merge Function
def merge(A, B):
  (m, n) = (len(A), len(B))
  (C, i, j, k) = ([], 0, 0, 0)
  while k < m + n:
    if i == m:
      C.extend(B[j:])
      k = k + (n-j)
    elif j == n:
      C.extend(A[i:])
      k = k + (m-i)
    elif A[i] < B[j]:
      C.append(A[i])
      (i,k) = (i+1,k+1)
    else:
      C.append(B[j])
      (j,k) = (j+1,k+1)
  return C


# Mergesort
def msort(A):
  n = len(A)
  if n <= 1:
    return A
  l = msort(A[:n//2])
  r = msort(A[n//2:])
  B = merge(l, r)
  return B
