

# can't live if livin' is without you
add = lambda x: lambda y: x + y
increment = add(1)
add_ten = add(10)

print(increment(2))
print(add_ten(2))

# using partial
from functools import partial
import re
match = (lambda what, s: re.match(what, s) is not None)
print(match('.*[r].*', 'hello world'))
has_letter_r = partial(match, '.*[r].*')
print(has_letter_r('hello world'))
print(has_letter_r('hello wold'))

replace = (lambda what, replacement, s: re.sub(what, replacement, s))
filter_c = (lambda f, xs: list(filter(f, xs)))
map_c = (lambda f, xs: list(map(f, xs)))

print(filter_c(has_letter_r, ['rock and roll', 'smooth jazz']))
remove_strings_without_rs = partial(filter_c, has_letter_r)
print(remove_strings_without_rs(['rock and roll', 'smooth jazz', 'drum circle']))

no_vowels = partial(replace, r'[aeiou]')
censored = partial(no_vowels, '*')
print(censored('Chocolate Rain'))
# using toolz curry




