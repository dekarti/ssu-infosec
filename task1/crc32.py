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
  for k in range(l - len(poly) + 1):
    if bits[0] == '1':
      for i in range(len(poly)):
        bits[i] = xor(bits[i], poly[i])
    bits = bits[1:]
  return bits



if __name__ == '__main__':

  sys.setrecursionlimit(100500)

  _type = sys.argv[1]
  if _type == '-s':
    msg = sys.argv[2]
  elif _type == '-f':
    with open(sys.argv[2], 'r') as myfile:
       msg = myfile.read()
  else:
    print "Invalid argument"
  

  import time
  start_time = time.time()
  

  bits = augment(bitarray(msg), 32)
  #print ''.join(bits)
  poly = list('100000100110000010001110110110111')
  hashsum = crc(bits, poly, 0, len(bits))
  print hex(int(''.join(hashsum), 2))

  #test = bitarray(msg) + hashsum
  #print ''.join(test) 
  #print ''.join(crc(test, poly, 0, len(bits)))
  print("--- %s seconds ---" % (time.time() - start_time))
