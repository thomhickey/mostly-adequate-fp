from typing import Callable
# Refactor to remove all arguments by partially applying the function.

# log :: int -> int
from functools import partial

log: Callable[[], float] = partial(pow, 10)

# tests
assert log(2) == 100
