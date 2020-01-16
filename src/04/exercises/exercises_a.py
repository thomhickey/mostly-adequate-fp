from typing import Callable

# Refactor to remove all arguments by partially applying the function.

# log :: int -> int
log: Callable[[int], float] = lambda num: pow(10, num)

# tests
assert log(2) == 100
