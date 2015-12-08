# emulate a damn circuit
import re
from ctypes import c_uint16 as uint16

sym_tab = {}
computed = {}
depth = []


def loop_check(s):
    if s in depth:
        raise Exception
    print depth
    depth.append(s)


def loop_clear(s):
    depth.remove(s)


def is_signal(x):
    return re.match(r'^\d+$', x) is not None


def is_wire(x):
    return re.match(r'^[a-z]+$', x) is not None


def and_op(x, y):
    return uint16(parse(x) & parse(y)).value


def or_op(x, y):
    return uint16(parse(x) | parse(y)).value


def lshift_op(x, y):
    return uint16(parse(x) << parse(y)).value


def rshift_op(x, y):
    return uint16(parse(x) >> parse(y)).value


def not_op(x):
    return uint16(~parse(x)).value


def get_re(op):
    return '(?P<lhs>[a-z]+|[0-9]+)\s+%s\s+(?P<rhs>[a-z]+|[0-9]+)' % op


not_re = re.compile(r'NOT\s+(?P<val>[a-z]+|[0-9]+)')
two_arg_ops = [{'n': 'and',
                're': re.compile(get_re('AND')),
                'op': and_op},
               {'n': 'or',
                're': re.compile(get_re('OR')),
                'op': or_op},
               {'n': 'lshift',
                're': re.compile(get_re('LSHIFT')),
                'op': lshift_op},
               {'n': 'rshift',
                're': re.compile(get_re('RSHIFT')),
                'op': rshift_op}]


def parse(token):
    if is_signal(token):
        return uint16(int(token)).value
    elif is_wire(token):
        loop_check(token)
        if token not in computed:
            computed[token] = parse(sym_tab[token])
        loop_clear(token)
        return computed[token]
    else:
        m = re.match(not_re, token)
        if m is not None:
            return not_op(m.groupdict()['val'])
        else:
            for x in two_arg_ops:
                m = re.match(x['re'], token)
                if m is not None:
                    return x['op'](m.groupdict()['lhs'], m.groupdict()['rhs'])

    print "parse error token %s" % token
    return None


def part_one():
    with open('day_7_input.txt', 'rb') as fh:
        ins = fh.read()
    inx = ins.split('\n')

    operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']
    split_re = re.compile(r'(?P<lhs>.+) -> (?P<rhs>.+)')
    for i in inx:
        m = re.match(split_re, i)
        if m is None:
            print 'ignored line: %s' % i
            continue
        md = m.groupdict()

        sym_tab[md['rhs']] = md['lhs']

    print parse('a')

part_one()
