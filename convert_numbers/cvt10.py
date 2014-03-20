import sys


def convert10(num10, to_base):
    num = num10
    num_base = ''
    while num >= to_base:
        denom = num // to_base
        rem = num % to_base
        #numBase = "[" + str(rem) + "]" + numBase
        num_base += digit_to_base(rem, to_base)
        num = denom
    #numBase = "[" + str(num) + "]" + numBase
    return digit_to_base(num, to_base) + num_base


def digit_to_base(digit, to_base):
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)


#------------------------------------------------
a = int(sys.argv[1])
base = 16
print("%d:10 = %s:%d" % (a, convert10(a, base), base))