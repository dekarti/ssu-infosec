#!/usr/bin/python

import sys

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


if __name__ == '__main__':

  sys.setrecursionlimit(100500)

  _type = sys.argv[1]
  if _type == '-s':
    msg = sys.argv[2]
  elif sys.argv[1] == '-f':
    with open(sys.argv[2], 'r') as myfile:
       msg = myfile.read()
  else:
    print "Invalid argument"

  bits = augment(bitarray(msg), 32)
  poly = list('100000100110000010001110110110111')
  hashsum = crc(bits, poly, 0, len(bits))
  print hex(int(''.join(hashsum), 2))

