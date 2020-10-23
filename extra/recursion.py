import sys
from functools import lru_cache

sys.setrecursionlimit(15000)
@lru_cache(128)
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
  print(fib(150))