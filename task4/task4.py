def binary_representation(c):
    return  bin(ord(c))[2:].zfill(8)


def to_bits(data):
    return ''.join(map(binary_representation, data))


def strip_line(lines):
    result = []
    for line in lines:
        result.append(line.rstrip())
    return result


def encrypt(bits, lines):
    result = []
    for i in range(len(bits)):
        if bits[i] == '1':
            result.append(lines[i] + ' ')
        else:
            result.append(lines[i] + '')
    return result


def decrypt(lines):
    res = ''
    bits = ''
    for line in lines:
        bits += '1' if len(line) and line[-1] == ' ' else '0'
        if len(bits) == 8:
            res += chr(int(bits, 2))
            bits = ''
    return res


if __name__ == "__main__":
    with open("4397-0.txt", "r") as f:
        lines = strip_line(f.readlines())
        print encrypt(lines)

