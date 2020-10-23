def convert_to_digits(num1: str):
  digits = int(num1[-1])
  count = 1
  for idx in range(len(num1) - 2, -1, -1):
    digits += int(num1[idx]) * pow(10, count)
    count += 1
  return digits

if __name__ == '__main__':
  print(convert_to_digits('12345'))