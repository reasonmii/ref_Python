'''
Merge
Merges two or more lists into a list of lists,
combining elements from each of the input lists based on their positions

- Use max() combined with a list comprehension
  to get the length of the longest list in the arguments
- Use range() in combination with the max_length variable
  to loop as many times as there are elements in the longest list
- If a list is shorter than max_length,
  use fill_value for the remaining items (defaults to None)
- zip() and itertools.zip_longest() provide similar functionality to this snippet

https://www.30secondsofcode.org/python/s/merge

*args
- 몇 개의 인자를 받을 지 알 수 없을 때
- *name 등 자유롭게 명명 가능
'''

def merge(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    rst = []
    for i in range(max_length):
        rst.append([args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))])
    return rst
    

# Examples
merge(['a','b'], [1,2], [True,False])  # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1,2], [True,False])      # [['a', 1, True], [None, 2, False]]
merge(['a'], [1,2], [True,False], fill_value='_')  # [['a', 1, True], ['_', 2, False]]
