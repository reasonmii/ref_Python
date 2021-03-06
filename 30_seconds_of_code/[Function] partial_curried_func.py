
'''
curry
Curries a function

- Use functools.partial() to return a new partial object
  which behaves like fn with the given arguments, args, partially applied

★ A curried function is a function which takes multiple parameters one at a time

https://www.30secondsofcode.org/python/s/curry
'''

from functools import partial

def curry(fn, *args):
    return partial(fn, *args)


# Example
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30


# reference =====================================================

def _sum(a, b):
    print(a + b)

f = partial(_sum, 20)
f(1)
# 21
