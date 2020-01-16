# Considering the following function:
# js: const keepHighest = (x, y) => (x >= y ? x : y);
keepHighest = lambda x, y: x if x >= y else y

# Refactor `max` to not reference any arguments using the helper function `keepHighest`.
# js:
# const max = xs => reduce((acc, x) => (x >= acc ? x : acc), -Infinity, xs);
# max :: [Number] -> Number
from functools import reduce
max = lambda xs: reduce(lambda acc, x: x if x >= acc else acc, xs, float("-inf"))

assert max([3, 4, 5]) == 5