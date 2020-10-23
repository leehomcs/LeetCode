def sort_stack(stack):
  tmp_stack = []
  while stack:
    tmp = stack.pop()
    if not tmp_stack or tmp_stack.peek() <= tmp:
      tmp_stack.append(tmp)
    else:
      while tmp_stack.peek() > tmp:
        stack.append(tmp_stack.pop())
      tmp_stack.append(tmp)
  while tmp_stack:
    stack.append(tmp_stack.pop())
  return stack