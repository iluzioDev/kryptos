def parseHex(number, n = 0):
  """
  Convert a number or a string to its hexadecimal representation.

  Args:
    number (int | str): The number or string to convert.
    n (int, optional): The number of hex digits to pad to. Defaults to 0.

  Raises:
    ValueError: If n is less than 0
    ValueError: If the number is not a positive integer

  Returns:
    str: The converted number or string.
  """
  if n < 0:
    raise ValueError('n must be a positive integer!')
  # Convert to string and remove spaces and colons
  number = str(number)
  if number.isnumeric():
    number = hex(int(number))
  number = number.upper().replace(' ', '').replace(':', '')
  # Cut the '0X' prefix if it exists
  if number[0:2] == '0X':
    number = number[2:]
  # Check if the string is a valid hexadecimal number
  for i in enumerate(number):
    if number[i] not in '0123456789ABCDEF':
      raise ValueError('Invalid hexadecimal number!')
  return number.zfill(n)

def split_by(element, n):
  """
  Splits a element into n-sized chunks.

  Args:
    element (str | list): The element to split.
    n (int): The size of the chunks.

  Raises:
    ValueError: If n is less than 1
    ValueError: If n is greater than the element length
    ValueError: If the element length is not a multiple of n

  Returns:
    list: A list of n-sized chunks of the element.
  """
  if n < 1:
    raise ValueError('n must be a positive integer!')
  if n > len(element):
    raise ValueError('n must be less than the element length!')
  if len(element) % n != 0:
    raise ValueError('String length is not a multiple of n!')
  return [element[i:i + n] for i in range(0, len(element), n)]

def split_words(element):
  """
  Splits a element into words.
  A word is defined as a group of 4 characters (or 2 bytes)

  Args:
    element (str | list): The element to split.
      
  Returns:
    list: A list of words of the element.
  """
  return split_by(split_by(element, 2), 4)

def truncate(number, n):
  """
  Truncates a number to n bits.

  Args:
    number (int): The number to truncate.
    n (int): The number of bits to truncate to.

  Returns:
    int: The truncated number.
  """
  return number & int('0x' + ('F' * n), 16)

def bitwise_shift(number, n, m, hex_digits):
  """
  Shifts a number n bits to the left, truncating the result to m bits.
  
  Args:
    number (int): The number to shift.
    n (int): The number of bits to shift.
    m (int): The number of bits to truncate to.
    hex_digits (int): The number of hex digits to truncate to.
  
  Raises:
    ValueError: If n is less than 0
    ValueError: If n is greater than m
    
  Returns:
    int: The shifted number.
  """
  if n < 0:
    raise ValueError('n must be a positive integer!')
  if n > m:
    raise ValueError('n must be less than the number of bits!')
  return (truncate(number << n, hex_digits)) | (number >> (m - n))
