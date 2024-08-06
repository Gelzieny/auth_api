import re

just_numbers = lambda a: ''.join(re.findall("\d+", a))

none_to_str = lambda a: '' if not a else str(a)
