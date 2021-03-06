
'''
1) union
Returns every element that exists in any of the two lists once

- Create a set with all values of a and b and convert to a list

https://www.30secondsofcode.org/python/s/union
'''

def union(a, b):
    return list(set(a+b))


# Example
union([1, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]


'''
2) union_by
Returns every element that exists in any of the two lists once,
after applying the provided function to each element of both

- Create a set by applying fn to each element in a
- Use a list comprehension in combination with fn on b to only keep values not contained in the previously created set, _a
- Finally, create a set from the previous result and a and transform it into a list

https://www.30secondsofcode.org/python/s/union-by
'''

def union_by(a, b, fn):
    _a = set(map(fn, a))
    return list(set(a + [item for item in b if fn(item) not in _a]))


# Example
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
