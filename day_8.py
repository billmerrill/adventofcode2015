import string
from pprint import pprint


def part_one():

    text_size = 0
    mem_size = 0
    esc_size = 0
    f = string.Formatter()

    def reencode(x):
        n = repr(x)
        n = n.replace('"', '\\"')
        # n = n.replace("'", "\\'")
        # n = '"%s"' % n
        return n

    # with open("day_8_sample.txt", 'rb') as fh:
    with open("day_8_input.txt", 'rb') as fh:
        for line in fh:
            l = line.strip()
            print l, eval(l), reencode(l), len(l), len(eval(l)), len(reencode(l))
            text_size += len(l)
            mem_size += len(eval(l))
            esc_size += len(reencode(l))

    a = {'text_size': text_size,
         'mem_size': mem_size,
         'esc_size': esc_size,
         'diff1': text_size - mem_size,
         'diff2': esc_size - text_size}
    pprint(a)

part_one()
