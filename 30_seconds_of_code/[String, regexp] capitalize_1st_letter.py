
'''
1) capitalize
Capitalizes the first letter of a string

- Use list slicing and str.upper() to capitalize the first letter of the string
- Use str.join() to combine the capitalized first letter
  with the rest of the characters
- Omit the lower_rest parameter to keep the rest of the string intact,
  or set it to True to convert to lowercase

https://www.30secondsofcode.org/python/s/capitalize
'''

def capitalize(s, lower_rest=False):
    return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])


# Example
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'


'''
2) decapitalize
Decapitalizes the first letter of a string

- Use list slicing and str.lower() to decapitalize the first letter of the string
- Use str.join() to combine the lowercase first letter with the rest of the characters
- Omit the upper_rest parameter to keep the rest of the string intact,
  or set it to True to convert to uppercase
  
https://www.30secondsofcode.org/python/s/decapitalize
'''

def decapitalize(s, upper_rest=False):
    return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])


# Example
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'


# reference =====================================================

s = 'fooBar'
s[:1]   # f
