
# Refactor to remove all arguments by partially applying the functions.

# js: const filterQs = xs => filter(x => x.match(/q/i), xs);
import re
filter_qs = lambda xs: list(filter(lambda x: re.match('.*[q].*', x), xs))


# tests
assert filter_qs(['abc', 'qrs']) == ['qrs']