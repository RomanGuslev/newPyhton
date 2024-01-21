_str = 'I am learning Python. hello, WORLD!'
start_range = _str.find('h')
end_range = _str.rfind('h')
not_reversed_part = _str[start_range + 1:end_range]
reversed_part = ''.join(reversed(not_reversed_part))
_str = _str.replace(not_reversed_part, reversed_part)
print(_str)