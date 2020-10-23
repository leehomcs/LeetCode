class Queue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []

  def size(self):
    return len(self.in_stack) + len(self.out_stack)

  def front(self):
    if self.out_stack:
      return self.out_stack[-1]
    else:
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
      return self.out_stack[-1]

  def push_back(self, element):
    self.in_stack.append(element)

  def pop_front(self):
    if self.out_stack:
      return self.out_stack.pop()
    else:
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
      return self.out_stack.pop()