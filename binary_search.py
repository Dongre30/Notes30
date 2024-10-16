def binarysearch(l, e):
  if l == []:
    return False
  mid = len(l)//2
  if e == l[mid]:
    return True
  if e < l[mid]:
    return binarysearch(l[:mid], e)
  else:
    return binarysearch(l[mid + 1:], e)
