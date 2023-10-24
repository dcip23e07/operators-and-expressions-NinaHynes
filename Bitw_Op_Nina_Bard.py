
def convert_to_base_2(n):
  """Converts a number to base 2.

  Args:
    n: The number to convert.

  Returns:
    A string representing the number in base 2.
  """

  base_2_string = ""
  while n > 0:
    remainder = n % 2
    base_2_string += str(remainder)
    n //= 2
  return base_2_string[::-1]

# Convert 4999 to base 2
print(convert_to_base_2(4999))

# Convert 2111 to base 2
print(convert_to_base_2(2111))

# What will be the value of 4999 & 2111
print(4999 & 2111)

# What will be the value of 4999 | 2111
print(4999 | 2111)