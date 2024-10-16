def selsort(A):
  n = len(A)
  if n < 1:
    return A
  for i in range(n):
    mpos = i
    for j in range(i+1, n):
      if A[j] < A[mpos]:
        mpos = j
    (A[i], A[mpos]) = (A[mpos], A[i])

  return A
