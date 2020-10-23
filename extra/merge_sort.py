def MergeSort(lists):
  if len(lists) <=1:
    return lists
  num = int(len(lists)/2)
  left = MergeSort(lists[:num])
  right = MergeSort(lists[num:])
  return merge(left, right)

def merge(left, right):
  r, l = 0,0
  result = []
  while l<len(left) and r<len(right):
    if left[l] < right[r]:
      result.append(left[l])
      l += 1
    else:
      result.append(right[r])
      r += 1
  # result.extend(left[l:])
  # result.extend(right[r:])
  result += list(left[l:])
  result += list(right[r:])
  return result

if __name__ == '__main__':
  res = MergeSort([1,2,3,4,5,6,7,90,21,23,45])
  print(res)