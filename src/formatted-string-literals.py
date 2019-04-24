from datetime import *

name = "Fred"

print(f"He said his name is {name!r}.")
print(f"He said his name is {repr(name)}.")     # repr() is equivalent to !r

# Conversion '!s' calls str() on the result, '!r' calls repr(), and '!a' calls ascii().


today = datetime(year=2017, month=1, day=27)
print(f"{today:%B %d, %Y}")                     # using date format specifier

number = 1024
print(f"{number:#0x}")                          # using integer format specifier
