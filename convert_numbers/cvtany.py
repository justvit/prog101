import string
import sys


def convert_to_10(num, from_base):
    power = len(num)
    result = 0
    for i in range(0,power):
        result += digit_from_base(num[i]) * (from_base ** (power - i - 1))
    return result


def convert_to_base(num_10, to_base):
    num = num_10
    result = ''
    while num >= to_base:
        den = num // to_base
        rem = num % to_base
        result += digit_to_base(rem)
        num = den
    return digit_to_base(num) + result


def convert(num, src_base, dest_base):
    num_10 = convert_to_10(num, src_base)
    return convert_to_base(num_10, dest_base) if dest_base != 10 else str(num_10)


def digit_to_base(digit_val):
    if digit_val < 10:
        return str(digit_val)
    else:
        return chr(ord('A') + digit_val - 10)


def digit_from_base(digit_char):
    if digit_char <= '9':
        return ord(digit_char) - ord('0')
    else:
        return ord(digit_char) - ord('A') + 10

#------------------------------------------------
src_arg = sys.argv[1]
dest_base = int(sys.argv[2])
[src_num,src_base] = src_arg.split(':')
src_num = src_num.upper()
src_base = int(src_base)

dest_num = convert(src_num, src_base, dest_base)

print("%s:%d = %s:%d" % (src_num, src_base, dest_num, dest_base))