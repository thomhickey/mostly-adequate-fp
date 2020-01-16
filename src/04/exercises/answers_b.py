# Refactor to remove all arguments by partially applying the functions.

# js: const filterQs = xs => filter(x => x.match(/q/i), xs);
import re
from functools import partial

filter_qs = partial(filter, partial(re.match, '.*[q].*'))  # dang, we can't return a list this way :(

# tests
assert list(filter_qs(['abc', 'qrs'])) == ['qrs']  # dang filter objects!
