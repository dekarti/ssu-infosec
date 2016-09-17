def bitarray(msg):
  chararray = [ list(bin(ord(c)))[2:] for c in list(msg) ]
  result = []
  for char in chararray:
    result += char
  return result

def xor(a, b):
  return '0' if a == b else '1'

def augment(bits, n):
  return bits + n * ['0']

def crc(bits, poly, k, l):
  if k == l - len(poly) - 1:  return bits;
  for i in range(len(poly)):
    bits[i] = xor(bits[i], poly[i])
  return crc(bits[1:], poly, k+1, l)


def crc32(msg):
  bits = augment(bitarray(msg), 32)
  print ''.join(bits)
  poly = list('100000100110000010001110110110111')
  print ''.join(poly)
  hashsum = ''.join(crc(bits, poly, 0, len(bits)))
  print hashsum
  print hex(int(hashsum, 2))

crc32("hello")
