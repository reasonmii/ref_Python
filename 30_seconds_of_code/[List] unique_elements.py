
'''
unique_elements
Returns the unique elements in a given list

- Create a set from the list to discard duplicated values,
  then return a list from it

https://www.30secondsofcode.org/python/s/unique-elements
'''

def unique_elements(lst):
    return list(set(lst))


# Example
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
