
'''
1) offset
Moves the specified amount of elements to the end of the list

- Use slice notation to get the two slices of the list
  and combine them before returning

https://www.30secondsofcode.org/python/s/offset
'''

def offset(lst, offset):    
    return lst[offset:] + lst[:offset]


# Example
offset([1, 2, 3, 4, 5], 2)   # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2)  # [4, 5, 1, 2, 3]


'''
2) roll
Moves the specified amount of elements to the start of the list.

- Use slice notation to get the two slices of the list
  and combine them before returning

https://www.30secondsofcode.org/python/s/roll
'''

def roll(lst, offset):    
    return lst[-offset:] + lst[:-offset]


# Example
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
