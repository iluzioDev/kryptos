def split_by(x, n):
  if n < 1:
    raise ValueError('n must be a positive integer!')
  if n > len(x):
    raise ValueError('n must be less than the string length!')
  if len(x) % n != 0:
    raise ValueError('String length is not a multiple of n!')
  return [x[i:i + n] for i in range(0, len(x), n)]

def split_into(x):
  return split_by(split_by(x, 2), 4)

def truncate(x, n):
  return x & int('0x' + ('F' * n), 16)

def left_rotate_n_bits(x, n, N_BITS, N_HEX):
  if n < 0:
    raise ValueError('n must be a positive integer!')
  if n > N_BITS:
    raise ValueError('n must be less than the number of bits!')
  return (truncate(x << n, N_HEX)) | (x >> (N_BITS - n))
