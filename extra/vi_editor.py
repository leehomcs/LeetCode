class Editor:
  def __init__(self, strings, cursor_pos):
    self.strings = strings
    self.cursor_pos = cursor_pos

  def cmd_h(self):
    x, y = self.cursor_pos
    if y > 0:
      y -= 1
    else:
      y = 0
    self.cursor_pos = [x, y]

  def print_file(self):
    for idx, line in enumerate(self.strings):
      if idx != self.cursor_pos[0]:
        print(line)
      else:
        pos = self.cursor_pos[1]
        new_line = line[:pos] + '^' + line[pos:]
        print(new_line)
    print('************************************')

if __name__ == '__main__':
  file1 = open('poem.txt', 'r')
  lines = file1.readlines() # read poem.txt content as a list
  lines = [line.strip('\n') for line in lines]
  #print(lines)
  cursor_pos = [0,3]
  vi_editor = Editor(lines, cursor_pos)
  print('The current file and cursor is as follows.')
  print('----------------------------------------')
  vi_editor.print_file()
  print('Please enter your command (e.g., type \'h\')')
  cmd = input()
  if cmd == 'h':
    vi_editor.cmd_h()
    vi_editor.print_file()