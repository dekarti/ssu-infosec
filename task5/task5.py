#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import codecs
import argparse
import fractions
import sys 

a = codecs.open('alphabet', 'r', 'utf-8')
final_alphabet = list(a.read())

def encrypt(s, k, n, m):
    # print s
    result = []
    for c in s:
        if c in final_alphabet:
            old_code = final_alphabet.index(c)
            new_code = (old_code * k + n) % m
            result.append(final_alphabet[new_code])
        else:
            result.append(c)
    return result


def decrypt(s, k, n, m):
    result = []
    for c in s:
        if c in final_alphabet:
            old_code = final_alphabet.index(c)
            count = 0
            inverse = 0
            while True:
                inverse = k * count % m
                if inverse == 1:
                    break;
                count += 1
            new_code = count * (old_code - n) % m
            result.append(final_alphabet[new_code])
        else:
            result.append(c)
    return result


def lowerize(s):
    return ''.join([
            c.lower()
            if c.lower() in final_alphabet
            else c
            for c in s ])

   
if __name__ == '__main__':

    mode = sys.argv[1]
    filename = sys.argv[2]
    print "Length of the alphabet is {}".format(len(final_alphabet))
    if mode == '-e':
        k = int(raw_input("Enter k: "))
        n = int(raw_input("Enter n: "))
        if not fractions.gcd(len(final_alphabet),n) == 1:
            print "Ошибка. НОД не равен 1"
        else:
            f =  codecs.open(filename, 'r', 'utf-8') 
            s = lowerize(f.read())
            s =  ''.join(encrypt(s, k, n, len(final_alphabet)))
            print s
            d = ''.join(decrypt(s, k, n, len(final_alphabet)))
            print d
