#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser()
command_parsers = parser.add_subparsers(help='Available commands', dest='command')
h = command_parsers.add_parser('encrypt', help='Hide file into another file')
h.add_argument('file', type=str, help='Input file to encrypt')
h.add_argument('container', type=str, help='Container wherein file will be encrypted')
h.add_argument('--output', '-o', type=str, help='Output filename')
r = command_parsers.add_parser('decrypt', help='Reveal encrypted file')
r.add_argument('input', type=str, help='Input file to decrypt')
r.add_argument('--output', '-o', type=str, help='Output file')


def prepare_for_encrypt(lines):
    return map(lambda x: x.rstrip(), lines)


def prepare_for_decrypt(lines):
    return map(lambda x: x.replace('\n', ''), lines)


def char_to_bin(c):
    return bin(ord(c))[2:].zfill(8)


def to_bits(data):
    return ''.join(map(char_to_bin, data))


def encrypt(bits, lines):
    return [lines[i] + (' ' if bits[i] == '1' else '') for i in range(len(bits))]


def decrypt(lines):
    bits = ''.join(map(lambda x: '1' if len(x) and x[-1] == ' ' else '0', lines))
    return ''.join(map(lambda x: chr(int(x, 2)), [bits[i:i+8] for i in range(0, len(bits), 8)]))


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    try:
        if args.command == 'encrypt':
            with open(args.container, "r") as f:
                lines = prepare_for_encrypt(f.readlines())
            with open(args.file, "r") as f:
                bits = to_bits(f.read())

            if len(lines) < len(bits):
                print 'Container too small. It contains only %d lines, but %d needed' % (len(lines), len(bits))
                quit(1)

            encrypted = encrypt(bits, lines)

            if args.output is None:
                for line in encrypted:
                    print line
            else:
                with open(args.output, 'w') as f:
                    for line in encrypted:
                        f.write(line + '\n')
        elif args.command == 'decrypt':
            with open(args.input, 'r') as f:
                lines = prepare_for_decrypt(f.readlines())
            decrypted = decrypt(lines)

            if args.output is None:
                print decrypted
            else:
                with open(args.output, 'w') as f:
                    f.write(decrypted)
    except Exception as e:
        print e.message, e.args
