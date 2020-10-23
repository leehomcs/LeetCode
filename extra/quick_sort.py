def quick_sort(data):
  if len(data) >= 2:
    mid = data[len(data)//2]
    left, right = [], []
    data.remove(mid)
    for num in data:
      if num >= mid:
        right.append(num)
      else:
        left.append(num)
    return quick_sort(left) + [mid] + quick_sort(right)
  else:
    return data

if __name__ == '__main__':
  array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
  print(quick_sort(array))