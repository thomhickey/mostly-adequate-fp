# Considering the following function:
# js: const keepHighest = (x, y) => (x >= y ? x : y);
keepHighest = lambda x, y: x if x >= y else y

# Refactor `max` to not reference any arguments using the helper function `keepHighest`.
# js:
# const max = xs => reduce((acc, x) => (x >= acc ? x : acc), -Infinity, xs);
from functools import reduce, partial

max = partial(reduce, keepHighest) # won't really work because we can't put -Infinity into the curried function :(

assert max([3, 4, 5]) == 5
