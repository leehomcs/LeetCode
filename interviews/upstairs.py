def num_upstairs(n, m):
  if n == m:
    return 1
  elif n > m:
    return 0
  else:
    return num_upstairs(n+1, m) + num_upstairs(n+2, m)

if __name__ == '__main__':

    m = 3
    print(num_upstairs(1, m))